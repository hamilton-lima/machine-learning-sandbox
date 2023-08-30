import json
import importlib.util
import os
import logging
from shutil import copyfile

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

SCRIPT_TEMPLATE_PATH = 'script_template.py'
SCRIPT_PATH = './scripts'

def load_scripts_from_json(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
    return data

def create_folder_if_not_exists(folder_path):
    if folder_path:
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

def create_script_if_not_exists(script_path):
    if not os.path.exists(script_path):
        copyfile(SCRIPT_TEMPLATE_PATH, script_path)

def run_script(script_name, input_folder, output_folder, model_folder=None):
    
    script_path = os.path.join(SCRIPT_PATH, script_name)
    create_script_if_not_exists(script_path)
    
    spec = importlib.util.spec_from_file_location(script_name, script_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    
    logging.info(f"START: {script_name}")
    logging.info(f"Input folder: {input_folder}")
    logging.info(f"Output folder: {output_folder}")
    if model_folder:
        logging.info(f"Model folder: {model_folder}")
    
    if hasattr(module, 'setup'):
        module.setup(input_folder, output_folder, model_folder)
    if hasattr(module, 'run'):
        module.run()
    logging.info(f"END: {script_name}")

def main():
    json_file = 'scripts.json'
    scripts_data = load_scripts_from_json(json_file)
    create_folder_if_not_exists(SCRIPT_PATH)    
    
    for script_info in scripts_data:
        input_folder = script_info['input_folder']
        script_name = script_info['script_name']
        output_folder = script_info['output_folder']
        model_folder = script_info.get('model', '')
        
        create_folder_if_not_exists(input_folder)
        create_folder_if_not_exists(output_folder)
        create_folder_if_not_exists(model_folder)
        
        run_script(script_name, input_folder, output_folder, model_folder)

if __name__ == "__main__":
    main()
