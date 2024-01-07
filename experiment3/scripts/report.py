# html_report_generator_updated.py
import os
import json
import logging
import base64

input = None
output = None

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def generate_html_report(input_folder, output_folder):
    validation_results_path = os.path.join(input_folder, 'validation_results.json')

    with open(validation_results_path, 'r') as json_file:
        validation_results = json.load(json_file)

    total_images = len(validation_results)
    success_count = sum(result["prediction_success"] for result in validation_results)
    success_percentage = (success_count / total_images) * 100 if total_images > 0 else 0

    # Calculate success rate per true label
    label_stats = {}
    for result in validation_results:
        label = result["true_label"]
        if label not in label_stats:
            label_stats[label] = {'total': 0, 'success': 0}
        label_stats[label]['total'] += 1
        if result["prediction_success"]:
            label_stats[label]['success'] += 1

    label_success_rates = {label: (
        stats['success'] / stats['total']) * 100 for label, stats in label_stats.items()}

    html_content = f'''
    <!DOCTYPE html>
    <html>
    <head>
        <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 2em;
        }}
        h1, h2 {{
            text-align: center;
        }}
        .summary, .label-summary {{
            font-weight: bold;
            text-align: center;
            margin-bottom: 1em;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
        }}
        th, td {{
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }}
        th {{
            background-color: #f2f2f2;
        }}
        .success {{
            background-color: #d0ffd0;
        }}
        .failure {{
            background-color: #ffd0d0;
        }}
        img {{
            max-width: 100px;
            max-height: 100px;
            width: auto;
            height: auto;
        }}
        </style>
    </head>
    <body>
        <h1>Validation Report</h1>
        <div class="summary">
            <p>Success Rate: {success_percentage:.2f}%</p>
        </div>
        <table>
            <tr>
                <th>Image</th>
                <th>Image Path</th>
                <th>True Label</th>
                <th>Predicted Label</th>
                <th>Predicted Probability</th>
                <th>Prediction Success</th>
            </tr>
    '''
    
    IMAGES_BASE_PATH='test-data'

    for result in validation_results:
        result_class = "success" if result["prediction_success"] else "failure"
        
        # Convert the image to base64 for embedding
        image_path = os.path.join(IMAGES_BASE_PATH, result["image_path"])
        with open(image_path, "rb") as image_file:
            image_data = base64.b64encode(image_file.read()).decode("utf-8")

        html_content += f'''
            <tr class="{result_class}">
                <td><img src="data:image/jpeg;base64,{image_data}"></td>
                <td>{result["image_path"]}</td>
                <td>{result["true_label"]}</td>
                <td>{result["predicted_label"]}</td>
                <td>{result["predicted_prob"]:.4f}</td>
                <td>{result["prediction_success"]}</td>
            </tr>
        '''

    # Add label success rates to the report
    html_content += '''
        </table>
        <h2>Success Rate by True Label</h2>
        <div class="label-summary">
        <table>
            <tr>
                <th>True Label</th>
                <th>Success Rate (%)</th>
            </tr>
    '''
    for label, rate in label_success_rates.items():
        html_content += f'''
            <tr>
                <td>{label}</td>
                <td>{rate:.2f}</td>
            </tr>
        '''
    html_content += '''
        </table>
        </div>
    </body>
    </html>
    '''

    html_report_path = os.path.join(output_folder, 'validation_report.html')
    with open(html_report_path, 'w') as html_file:
        html_file.write(html_content)

def setup(input_folder, output_folder, model_folder=None):
    global input, output, model
    input = input_folder
    output = output_folder
    model = model_folder
    logging.info(f"Setting up: input_folder={input_folder}, output_folder={output_folder}, "
                 f"model_folder={model_folder}")

def run():
    global input, output, model
    logging.info(f"Running: {__name__}")
    logging.info(f"With parameters: input={input}, output={output}, model={model}")
    generate_html_report(input, output)

# End of the script
