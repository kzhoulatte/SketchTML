# This is the part to automatically generate screenshots from html codes and save the sketches as png files for later processing: 

import os  
import webbrowser
from selenium import webdriver

from argparse import ArgumentParser


parser = ArgumentParser()
parser.add_argument('--html_input_path', type=str,
                        dest='html_input_path', help='directory for HTML files and gui files',
                        default='./html_generated/')
parser.add_argument('--gui_input_path', type=str,
                        dest='gui_input_path', help='directory for HTML files and gui files',
                        default='./gui_generated/')
parser.add_argument('--screenshot_output_path', type=str,
                        dest='screenshot_output_path', help='directory for screenshots',
                        default='./screenshots/')


options = parser.parse_args()

html_dir = options.html_input_path
gui_dir = options.gui_input_path
screen_dir = options.screenshot_output_path


browser = webdriver.Chrome()

#browser.set_window_position(0, 0)
browser.set_window_size(1200, 1000)

#JavascriptExecutor js = (JavascriptExecutor) browser;
#js.executeScript("document.body.style.zoom='90%'");
#browser.execute_script("document.body.style.zoom='20 %'")

path_folder = 'file://'+os.getcwd()+html_dir.split('.')[1]

print(path_folder)

if not os.path.exists(screen_dir):
    os.makedirs(screen_dir)

for html in os.listdir(html_dir):
    
    path = path_folder + html
    browser.get(path)
    
    html_name = html.split('.')[0]
    browser.save_screenshot(screen_dir+html_name+'.png')
    
browser.close()
print('All sketches saved. \n')