# script_template.py
import logging
import tensorflow as tf 
import matplotlib.pyplot as plt
import numpy as np 
import os

from tensorflow.keras.preprocessing.image import ImageDataGenerator 
from tensorflow.keras.preprocessing import image
from tensorflow.keras.optimizers import RMSprop

input = None
output = None
model = None

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def setup(input_folder, output_folder, model_folder=None):
    global input, output, model
    input = input_folder
    output = output_folder
    model = model_folder
    logging.info(f"Setting up: input_folder={input_folder}, output_folder={output_folder}, "
                 f"model_folder={model_folder}")
    
def train_model(input_folder, output_folder):
    train = ImageDataGenerator(rescale=1/255)
    validation = ImageDataGenerator(rescale=1/255)

    train_path = input_folder
    validation_path = input_folder 
    # 'test-data'
    logging.info(f"train_path={train_path}")
    logging.info(f"validation_path={validation_path}")
    
    train_dataset = train.flow_from_directory(train_path, 
                                            target_size=(200,200), 
                                            batch_size=3, 
                                            class_mode = 'binary')

    validation_dataset = train.flow_from_directory(validation_path, 
                                            target_size=(200,200), 
                                            batch_size=3, 
                                            class_mode = 'binary')
    
    logging.info(f"CLASS INDICES ={train_dataset.class_indices}")
    
    model = tf.keras.models.Sequential( [ 
        tf.keras.layers.Conv2D(16,(3,3), activation = 'relu', input_shape= (200,200,3)), 
        tf.keras.layers.MaxPool2D(2,2),
        tf.keras.layers.Conv2D(32,(3,3), activation = 'relu'), 
        tf.keras.layers.MaxPool2D(2,2),
        tf.keras.layers.Conv2D(64,(3,3), activation = 'relu'), 
        tf.keras.layers.MaxPool2D(2,2),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(512, activation = 'relu'), 
        tf.keras.layers.Dense(1, activation = 'sigmoid')
    ])

    model.compile(loss= 'binary_crossentropy', optimizer = RMSprop(lr=0.001), metrics=['accuracy'])

    model_fit = model.fit( train_dataset, 
                        steps_per_epoch = 3, 
                        epochs = 70, 
                        validation_data = validation_dataset)  
    
    # Save the trained model in the output_folder
    model.save(os.path.join(output_folder, 'trained_model.h5'))      

def run():
    global input, output, model
    logging.info(f"Running: {__name__}")
    logging.info(f"With parameters: input={input}, output={output}, model={model}")

    train_model(input,output)