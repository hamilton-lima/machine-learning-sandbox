# script_template.py
import logging
import os
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from PIL import Image

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
    datagen = ImageDataGenerator(rescale=1./255)

    original_img = Image.open(input_image)
    original_img_array = original_img.convert("RGB")
    original_img_array = (np.array(original_img_array)).astype('float32')
    
    input_subfolder = os.path.relpath(os.path.dirname(input_image), input_folder)
    
    for version in range(num_versions):
        rotation_angle = version * rotation_step
        rotated_img_array = datagen.apply_transform(original_img_array, {'theta': rotation_angle})
        rotated_img = Image.fromarray(rotated_img_array.astype('uint8'))

        output_subfolder = os.path.join(output_folder, input_subfolder)
        os.makedirs(output_subfolder, exist_ok=True)
        
        output_filename = f"version_{version+1:02d}_{os.path.basename(input_image)}"
        output_path = os.path.join(output_subfolder, output_filename)
        rotated_img.save(output_path)
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


