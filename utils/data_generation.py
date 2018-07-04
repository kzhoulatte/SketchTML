# This script is to generate more GUI and html codes simultaneously for hand drawings and GUI datasets. 

import random
import string
import os
from argparse import ArgumentParser


parser = ArgumentParser()

parser.add_argument('--html_output_path', type=str,
                        dest='html_output_path', help='directory for HTML files and gui files',
                        default='./html_generated/')
parser.add_argument('--gui_output_path', type=str,
                        dest='gui_output_path', help='directory for HTML files and gui files',
                        default='./gui_generated/')

parser.add_argument('--size_of_data', type=int,
                        dest='size_of_data', help='size of total data to generate',
                        default=1000)

options = parser.parse_args()

html_train = options.html_output_path
gui_train = options.gui_output_path

size_data = options.size_of_data


num2boxes = ['single','double','quadruple']
link2str = ['one','two','three']


if not os.path.exists(html_train):
    os.makedirs(html_train)

if not os.path.exists(gui_train):
    os.makedirs(gui_train)


for i in range(size_data):
   
    num_navs = random.randint(1,5)

    index_boxes = random.randint(0,2)
    num_boxes = num2boxes[index_boxes]
    
    file_path_gui = gui_train+str(i)+'.gui'
    file_path_html = html_train+str(i)+'.html'

    with open(file_path_gui,'w+') as f:
        with open(file_path_html,'w+') as f2:

            f.write('header { \n')
            header = open('./html_header.html','r') 
            
            for line in header:
                f2.write(line)
                
            f2.write('\n')
            f2.write('<div class="header clearfix"> \n')
            f2.write('<nav> \n')
            f2.write('<ul class="nav nav-pills pull-left"> \n')
            
            for j in range(num_navs):
                f.write('btn-active ')
                random_str = ''.join([random.choice(string.ascii_letters  + string.digits ) for n in range(8)]) #8
                f2.write('<li><a href="#">'+random_str+'</a></li> \n')
                if j<num_navs-1:
                    f.write(', ')

            f.write('\n} \n')
            f2.write('</ul> \n')
            f2.write('</nav> \n')
            f2.write('</div> \n')
        
# ROW boxes: 
            
            rownumber = random.randint(2,3)
            for rows in range(rownumber):
                
                index_boxes = random.randint(0,2)
                num_boxes = num2boxes[index_boxes]
            
                f.write('row { \n')
                f2.write('<div class="row"> \n')

                if num_boxes == 'single':
                    for t in range(1):

                        f.write('single  {  \n')
                        
                        f2.write('<div class="col-lg-12"> \n')
                        f.write('small-title,  ')
                        random_str = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(8)]) #8
                        random_str2 = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(64)]) #64
                        f2.write('<h4>'+random_str+'</h4><p>'+random_str2+'</p> \n')
                        f.write('text  ')
                        btn = random.randint(0,3)
                        link = random.randint(1,3)
                        if btn == 1:
                            f.write(', ')
                            f.write('btn-orange '+'\n')
                            random_str = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(8)]) #8
                            f2.write('<a class="btn" style="height:60px;width:150px" href="#" role="button">'+random_str+'</a> \n')
                        elif link > 0:
                            f.write(', ')
                            linkstr = link2str[link-1]
                            f.write('link-'+linkstr+' \n')
                            f2.write('<a class="btn sketchTMLwide" href="'+str(link)+'.html" role="button"><div class="sketchTMLclickCircle">'+str(link)+'</div></a> \n')
                        f.write('} \n')
                        f2.write('</div> \n')
    
                if num_boxes == 'double':
                    for t in range(2):
                    
                        f.write('double { \n')
                        
                        f2.write('<div class="col-lg-6"> \n')
                        f.write('small-title,  ')
                        random_str = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(8)]) #8
                        random_str2 = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)]) #32
                        f2.write('<h4>'+random_str+'</h4><p>'+random_str2+'</p> \n')
                        f.write('text  ')
                        btn = random.randint(0,3)
                        link = random.randint(1,3)
                        if btn == 1:
                            f.write(', ')
                            f.write('btn-orange \n')
                            random_str = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(8)]) #8
                            f2.write('<a class="btn" style="height:60px;width:150px" href="#" role="button">'+random_str+'</a> \n')
                        elif link > 0:
                            f.write(', ')
                            linkstr = link2str[link-1]
                            f.write('link-'+linkstr+' \n')
                            f2.write('<a class="btn sketchTMLwide" href="'+str(link)+'.html" role="button"><div class="sketchTMLclickCircle">'+str(link)+'</div></a> \n')
                        f.write('} \n')
                        f2.write('</div> \n')
            
                if num_boxes == 'quadruple':
                    for t in range(4):
                    
                        f.write('quadruple { \n')
                        f2.write('<div class="col-lg-3"> \n')
                        f.write('small-title,  ')
                        random_str = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(8)]) #8
                        random_str2 = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(16)]) #16
                        f2.write('<h4>'+random_str+'</h4><p>'+random_str2+'</p> \n')
                        f.write('text  ')
                        btn = random.randint(0,3)
                        link = random.randint(1,3)
                        if btn == 1:
                            f.write(', ')
                            f.write('btn-orange \n')
                            random_str = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(8)]) #8
                            f2.write('<a class="btn" style="height:60px;width:150px" href="#" role="button">'+random_str+'</a> \n')
                        elif link > 0:
                            f.write(', ')
                            linkstr = link2str[link-1]
                            f.write('link-'+linkstr+' \n')
                            f2.write('<a class="btn sketchTMLwide" href="'+str(link)+'.html" role="button"><div class="sketchTMLclickCircle">'+str(link)+'</div></a> \n')
                        f.write('} \n')
                        f2.write('</div> \n')
            
                f.write('} \n')
                f2.write('</div> \n')
        
            f2.write('</main> \n')
            f2.write('<script src="js/jquery.min.js"></script> \n')
            f2.write('<script src="js/bootstrap.min.js"></script> \n')
            f2.write('</section> \n')
            f2.write('</body> \n')
            f2.write('</html> \n')      
        
            header.close()
            f.close()
            f2.close()
        
print('All datas generated. \n')
           
