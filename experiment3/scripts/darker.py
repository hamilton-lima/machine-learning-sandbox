# script_template_darker.py
import logging
import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageEnhance

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


def generate_darker_images(input_image, input_folder, output_folder, gamma_factor=1.5):
    
    image = Image.open(input_image)
    input_subfolder = os.path.relpath(os.path.dirname(input_image), input_folder)
    
    enhancer = ImageEnhance.Brightness(image)
    darker_image = enhancer.enhance(0.5)  # Darken the image by setting the brightness to 50%
    
    output_subfolder = os.path.join(output_folder, input_subfolder)
    os.makedirs(output_subfolder, exist_ok=True)
    
    output_filename = f"darker_{os.path.basename(input_image)}"
    output_path = os.path.join(output_subfolder, output_filename)
    output_path_original = os.path.join(output_subfolder, os.path.basename(input_image))
    
    darker_image.save(output_path)
    image.save(output_path_original)
    
    logging.info(f"Generated and saved: {output_path}")
    logging.info(f"Copied             : {output_path_original}")

def generate_darker_images_for_folder(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    
    for root, _, files in os.walk(input_folder):
        for filename in files:
            if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                input_path = os.path.join(root, filename)
                generate_darker_images(input_path, input_folder, output_folder)
                
def run():
    global input, output, model
    logging.info(f"Running: {__name__}")
    logging.info(f"With parameters: input={input}, output={output}, model={model}")
    generate_darker_images_for_folder(input, output)
