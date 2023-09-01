# script_template.py
import logging
import os
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from PIL import Image
from scipy import ndimage
import matplotlib.pyplot as plt

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


def generate_rotated_images(input_image, input_folder, output_folder, num_versions=8, rotation_step=45):
    image = plt.imread(input_image)
    input_subfolder = os.path.relpath(os.path.dirname(input_image), input_folder)
    
    for version in range(num_versions):
        rotation_angle = version * rotation_step
        rotated_image = ndimage.rotate(image, rotation_angle)

        output_subfolder = os.path.join(output_folder, input_subfolder)
        os.makedirs(output_subfolder, exist_ok=True)
        
        output_filename = f"version_{version+1:02d}_{os.path.basename(input_image)}"
        output_path = os.path.join(output_subfolder, output_filename)
        plt.imsave(output_path, rotated_image)

        logging.info(f"Generated and saved: {output_path}")

def generate_rotated_images_for_folder(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    
    for root, _, files in os.walk(input_folder):
        for filename in files:
            if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                input_path = os.path.join(root, filename)
                generate_rotated_images(input_path, input_folder, output_folder)
                
def run():
    global input, output, model
    logging.info(f"Running: {__name__}")
    logging.info(f"With parameters: input={input}, output={output}, model={model}")
    generate_rotated_images_for_folder(input, output)


