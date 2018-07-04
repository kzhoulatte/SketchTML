from flask import Flask
app = Flask(__name__)
from flaskapp import views

#model = views.loadmodel()

user = 'KZ' 
UPLOAD_FOLDER = 'flaskapp/static/images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
