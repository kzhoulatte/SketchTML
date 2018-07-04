
# SketchTML 

Generating clickable HTML website from hand drawnings using deep learning. 

## Prepare your environment:  

 - Python 3.6 is recommended; 

 - To install dependencies: 

&nbsp; &nbsp; pip install -r requirements.txt

 - To install tensorflow with GPU support: 

&nbsp; &nbsp; Install Anaconda 

&nbsp; &nbsp; conda install -c anaconda tensorflow-gpu

## Data Generation: 

 - Generate HTML and GUI files: 
 
&nbsp; &nbsp; python data_generation.py --html_output_path ./html_generated/ --gui_output_path ./gui_generated/ --size_of_data 1000

 - Generate screenshots as sketches: 
 
&nbsp; &nbsp; python sketches_generation.py --html_input_path ./html_generated/ --gui_input_path ./gui_generated/ --screenshot_output_path ./screenshots/



## Training: 

cd ./utils/ <br/>
python data_generation.py <br/>
python sketches_generation.py <br/>
sh ./move_data.sh <br/> 
cd .. <br/> 
cd ./src/ <br/>

 - From scratch: 

python train.py --data_input_path './classes/dataset/data/' <br/>
&nbsp; &nbsp;       --validation_split 0.2 <br/>
&nbsp; &nbsp;       --epochs 10 <br/>
&nbsp; &nbsp;       --model_output_path './' <br/>
&nbsp; &nbsp;       --augment_training_data 1


 - From pre-trained-model:

python train.py --data_input_path './classes/datasets/data/' <br/>
&nbsp; &nbsp;      --validation_split 0.2 <br/>
&nbsp; &nbsp;      --epochs 10 <br/>
&nbsp; &nbsp;      --model_output_path './' <br/>
&nbsp; &nbsp;      --model_json_file ./bin/model_json.json <br/>
&nbsp; &nbsp;      --model_weights_file ./bin/pretrained_weights.h5 <br/>
&nbsp; &nbsp;      --augment_training_data 1

## Evaluation: 

- evaluate single GUI prediction

python evaluate_single_gui.py --original_gui_filepath  {path/to/original/gui/file}  --predicted_gui_filepath {path/to/predicted/gui/file}

- evaluate batch GUI prediction

python evaluate_batch_guis.py --original_guis_filepath  {path/to/folder/with/original/guis} --predicted_guis_filepath {path/to/folder/with/predicted/guis}

