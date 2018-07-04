from flask import render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from flaskapp import app
import numpy as np
import tensorflow as tf
from keras.models import load_model, model_from_json
import cv2

from classes.dataset.Dataset import *
from classes.dataset.ImagePreprocessor import *
from classes.inference.Evaluator import *
from classes.inference.Compiler import *
from classes.inference.Sampler import *

from nltk.translate.bleu_score import sentence_bleu, corpus_bleu

import zipfile
import io
import pathlib

import flask as fl

#from src.classes.inference.Sampler import * 

import os
import shutil

MAX_LENGTH = 48


#print(UPLOAD_FOLDER)

ALLOWED_EXTENSIONS = set([ 'png', 'jpg'])

user = 'KZ' 
UPLOAD_FOLDER = 'flaskapp/static/images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

model_json_file = './model/model.json'
model_weights_file = './model/weights.h5'

#global uploaded_imgs

uploaded_imgs = 0

#app = Flask(__name__)

#photos = UploadSet('photos',IMAGES)
#configure_uploads(app,photos)


def allowed_file(filename):
		return '.' in filename and \
					 filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def loadmodel():

		json_file = open(model_json_file, 'r')
		loaded_model_json = json_file.read()
		json_file.close()
		loaded_model = model_from_json(loaded_model_json)
		loaded_model.load_weights(model_weights_file)
		print("\nLoaded model from disk")
		return loaded_model

		#sampler = Sampler(model_json_path=model_json_file,
		#                  model_weights_path = model_weights_file)
		#sampler.convert_single_image(output_folder, png_path=pngs_path,  get_sentence_bleu=print_bleu_score, original_gui_filepath=original_guis_filepath, style=style)


@app.route('/')
@app.route('/index')
def index():
		return render_template("index.html")

@app.route('/about')
def about():
		#profile = 'flaskapp/static/imgs/profile.jpg'
		return render_template("about.html")#, profile_image=profile)


@app.route('/upload', methods=['GET', 'POST'])
def upload_image():
		if request.method == 'POST':
				# check if the post request has the file part
				if 'img_file_path' not in request.files:
						flash('No file part')
						return redirect(request.url)
				file = request.files['img_file_path']
				# if user does not select file, browser also
				# submit a empty part without filename
				if file.filename == '':
						flash('No selected file')
						return redirect(request.url)
				if file and allowed_file(file.filename):
						filename = secure_filename(file.filename)
						order = sum([int(s) for s in list(filename) if s.isdigit()])
						if os.path.exists('flaskapp/static/images/'+str(order)+'.png'):
							os.remove('flaskapp/static/images/'+str(order)+'.png')
						if os.path.exists('flaskapp/templates/'+str(order)+'.gui'):
							os.remove('flaskapp/templates/'+str(order)+'.gui')
						if os.path.exists('flaskapp/templates/'+str(order)+'.html'):
							os.remove('flaskapp/templates/'+str(order)+'.html')
						if os.path.exists('./output/'+str(order)+'.html'):
							os.remove('./output/'+str(order)+'.html')

						#print(app.config['UPLOAD_PHOTOS_DEST'])
						file.save(os.path.join('flaskapp/static/images', str(order)+'.png'))
						#uploaded_imgs += 1
						#print('uploaded images:')
						#print(uploaded_imgs)
						imgfile = {"filepath": os.path.join("images",filename)}
						print(imgfile)
						result = 'Sketch ' + filename + ' uploaded. '

						return render_template("index.html", title="Home", content0 = result)
		return


@app.route('/generate', methods=['GET', 'POST'])
def convert_batch_of_images():
		if request.method == 'POST':
			output_folder = 'flaskapp/templates'
			pngs_path = 'flaskapp/static/images'
			print_bleu_score = 0
			original_guis_filepath =  None
			style = 'default'


			if not os.path.exists(output_folder):
				os.makedirs(output_folder)

			# Create sampler
			sampler = Sampler(model_json_path=model_json_file,
						model_weights_path = model_weights_file)

			# Sample and retrieve BLEU
			sampler.convert_batch_of_images(output_folder, pngs_path=pngs_path, get_corpus_bleu=print_bleu_score, original_guis_filepath=original_guis_filepath, style=style)

			print('HTML codes generated.')

			result = 'HTML codes generated!'

			#uploaded_imgs = 0

			return render_template("index.html", title="Home",content1 = result )
		

@app.route('/website', methods=['GET', 'POST'])
def website_html0():
	if request.method == 'POST':
		return render_template('0.html',title='Website')

@app.route('/1.html')
def website_html1():
	return render_template('1.html',title='Website')

@app.route('/2.html')
def website_html2():
	return render_template('2.html',title='Website')

@app.route('/3.html')
def website_html3():
	return render_template('3.html',title='Website')

@app.route('/download', methods=['GET', 'POST'])
def download_zip():
	if request.method == 'POST':


		# For purpose of Demo, this part is explicitly written for only 4 images. 
		shutil.copy('flaskapp/templates/0.html','./output/0.html')
		shutil.copy('flaskapp/templates/1.html','./output/1.html')
		shutil.copy('flaskapp/templates/2.html','./output/2.html')
		shutil.copy('flaskapp/templates/3.html','./output/3.html')

		#shutil.copy('flaskapp/templates/0.gui','./output/0.gui')
		#shutil.copy('flaskapp/templates/1.gui','./output/1.gui')
		#shutil.copy('flaskapp/templates/2.gui','./output/2.gui')
		#shutil.copy('flaskapp/templates/3.gui','./output/3.gui')

		base_path = pathlib.Path('./output/')
		print(base_path)
		htmls = io.BytesIO()
		print(htmls)
		with zipfile.ZipFile(htmls, mode='w') as z:
			for f_name in base_path.iterdir():
				z.write(f_name)
		htmls.seek(0)
		return fl.send_file(
			htmls,
			mimetype='application/zip',
			as_attachment=True,
			attachment_filename='htmls.zip'
		)


