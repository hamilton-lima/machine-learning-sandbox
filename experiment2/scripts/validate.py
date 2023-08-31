# validation_script_updated.py
import os
import json
import logging
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

input = None
output = None
model = None

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def setup(input_folder, output_folder, model_path):
    global input, output, model
    input = input_folder
    output = output_folder
    model = model_path
    logging.info(f"Setting up: input_folder={input_folder}, output_folder={output_folder}, "
                 f"model_path={model_path}")

def validate_model(input_folder, output_folder):
    test_data_gen = ImageDataGenerator(rescale=1/255)
    test_path = input_folder

    test_dataset = test_data_gen.flow_from_directory(test_path,
                                                     target_size=(200, 200),
                                                     batch_size=1,
                                                     class_mode='binary',
                                                     shuffle=False)

    loaded_model = tf.keras.models.load_model(model)

    results = []
    for i in range(len(test_dataset)):
        image_path = test_dataset.filenames[i]
        image_data = test_dataset[i][0]
        true_label = test_dataset[i][1][0]

        predicted_prob = loaded_model.predict(image_data)[0][0]
        predicted_label = int(predicted_prob >= 0.5)

        if true_label == predicted_label:
            prediction_success = True
        else:
            prediction_success = False

        result = {
            "image_path": image_path,
            "true_label": int(true_label),
            "predicted_label": predicted_label,
            "predicted_prob": float(predicted_prob),
            "prediction_success": prediction_success
        }
        results.append(result)

    # Save the validation results as a JSON file in the output_folder
    validation_results_path = os.path.join(output_folder, 'validation_results.json')
    with open(validation_results_path, 'w') as json_file:
        json.dump(results, json_file, indent=4)

def run():
    global input, output, model
    logging.info(f"Running: {__name__}")
    logging.info(f"With parameters: input={input}, output={output}, model={model}")
    validate_model(input, output)
    
