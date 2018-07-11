
# SketchTML 

Generating clickable HTML website from hand drawnings using deep learning 

![alt text][example]

[example]: https://github.com/kzhoulatte/SketchTML/blob/master/webapp/flaskapp/static/imgs/example.png

## Prepare your environment:  

 - Python 3.6 is recommended; 

 - To install dependencies: 
```
pip install -r requirements.txt
```
 - To install tensorflow with GPU support using Anaconda: 
```
conda install -c anaconda tensorflow-gpu
```
## Data Generation: 

 - Generate HTML and GUI files: 
``` 
python data_generation.py --html_output_path {path/to/html/output} --gui_output_path {path/to/gui/output} --size_of_data 1000
```
 - Generate screenshots as sketches: 
``` 
python sketches_generation.py --html_input_path {path/to/html/output} --gui_input_path {path/to/gui/output} --screenshot_output_path {path/to/screenshots/output}
```
* Large computer screen is recommended for auto screenshots to work perfectly. 

## Training: 

 - Move generated data for training: 
```
sh ./move_data.sh 
cd ../src/ 
```
 - Train from scratch: 
```
python train.py --data_input_path './classes/dataset/data/' 
          --validation_split 0.2
          --epochs 10 
          --model_output_path './' 
          --augment_training_data 1
```

 - Train from pre-trained-model:
```
python train.py --data_input_path './classes/datasets/data/' 
          --validation_split 0.2 
          --epochs 10 
          --model_output_path './' 
          --model_json_file ./bin/model_json.json 
          --model_weights_file ./bin/pretrained_weights.h5 
          --augment_training_data 1
```
## Evaluation: 

- evaluate single GUI prediction
```
python evaluate_single_gui.py --original_gui_filepath  {path/to/original/gui/file}  --predicted_gui_filepath {path/to/predicted/gui/file}
```
- evaluate batch GUI prediction
```
python evaluate_batch_guis.py --original_guis_filepath  {path/to/folder/with/original/guis} --predicted_guis_filepath {path/to/folder/with/predicted/guis}
```
## Web APP:

Please navigate to sketchtml.fun

![alt text][webapp]

[webapp]: https://github.com/kzhoulatte/SketchTML/blob/master/webapp/flaskapp/static/imgs/webapp.png
