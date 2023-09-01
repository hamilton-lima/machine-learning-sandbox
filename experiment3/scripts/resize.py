# script_template.py
import logging
import os
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

def resize_images(input_folder, output_folder, target_size):
    for root, _, files in os.walk(input_folder):
        for filename in files:
            if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                input_path = os.path.join(root, filename)
                output_subfolder = os.path.relpath(root, input_folder)
                output_subfolder_path = os.path.join(output_folder, output_subfolder)
                os.makedirs(output_subfolder_path, exist_ok=True)
                output_path = os.path.join(output_subfolder_path, filename)
                
                try:
                    with Image.open(input_path) as img:
                        img.thumbnail(target_size)
                        img.save(output_path)
                        logging.info(f"Resized and saved: {output_path}")
                except Exception as e:
                    logging.error(f"Error processing {input_path}: {e}")

def run():
    global input, output, model
    logging.info(f"Running: {__name__}")
    logging.info(f"With parameters: input={input}, output={output}, model={model}")

    target_size = (200, 200)
    resize_images(input, output, target_size)
