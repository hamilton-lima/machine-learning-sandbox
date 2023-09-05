import cv2
import numpy as np
import logging
import argparse
import os
import json
from datetime import datetime
import time

def setup_logging():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s]: %(message)s")

def detect_bubbles(image_path):
    logging.info("Starting bubble detection.")

    # Read the image
    logging.info(f"Reading image from {image_path}.")
    img_original = cv2.imread(image_path, cv2.IMREAD_COLOR)

    # Convert the image to grayscale
    logging.info("Converting image to grayscale.")
    gray = cv2.cvtColor(img_original, cv2.COLOR_BGR2GRAY)

    # Threshold the image to binary
    logging.info("Applying binary thresholding.")
    _, thresh = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)

    # Contour modes
    contour_modes = [cv2.RETR_EXTERNAL, cv2.RETR_LIST, cv2.RETR_CCOMP, cv2.RETR_TREE]
    contour_mode_names = ["RETR_EXTERNAL", "RETR_LIST", "RETR_CCOMP", "RETR_TREE"]

    # Result folder
    result_folder = "result"
    if not os.path.exists(result_folder):
        logging.info("Creating result folder.")
        os.makedirs(result_folder)

    # Extract the original file name (without extension) from the image_path
    original_file_name = os.path.splitext(os.path.basename(image_path))[0]

    # Current timestamp
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

    summary = []

    for mode, mode_name in zip(contour_modes, contour_mode_names):
        logging.info(f"Finding contours using {mode_name} mode.")

        # Start measuring time
        start_time = time.time()

        contours, _ = cv2.findContours(thresh.copy(), mode, cv2.CHAIN_APPROX_SIMPLE)

        # Stop measuring time
        end_time = time.time()
        time_elapsed = end_time - start_time
        time_elapsed = (end_time - start_time) * 1000 
        logging.info(f"{mode_name} took {time_elapsed} miliseconds to identify the contours.")

        img = img_original.copy()

        bubble_details = []

        for contour in contours:
            if cv2.contourArea(contour) < 50:
                continue

            # Draw contours in red
            cv2.drawContours(img, [contour], -1, (0, 0, 255), 1)

            # Fit a circle to the contour and draw it
            ((x, y), radius) = cv2.minEnclosingCircle(contour)
            cv2.circle(img, (int(x), int(y)), int(radius), (0, 255, 0), 2)

            # Record the bubble details (x, y, size)
            bubble_details.append({"x": x, "y": y, "size": radius})

        # Save the output image
        output_filename = f"{result_folder}/{mode_name}-detect-test2-{original_file_name}-{timestamp}.jpg"
        logging.info(f"Saving the output image to {output_filename}.")
        cv2.imwrite(output_filename, img)

        # Save the bubble details to a JSON file
        json_filename = f"{result_folder}/{mode_name}-detect-test2-{original_file_name}-{timestamp}.json"
        logging.info(f"Saving the bubble details to {json_filename}.")
        with open(json_filename, 'w') as f:
            json.dump(bubble_details, f)

        summary.append({
            'mode': mode_name,
            'time': time_elapsed,
            'bubbles': len(bubble_details)
        })

    logging.info("Bubble detection completed.")

    # Print Summary
    logging.info("=== Summary ===")
    for entry in summary:
        logging.info(f"{entry['mode']}: {entry['bubbles']} bubbles found, took {entry['time']} miliseconds")

if __name__ == "__main__":
    setup_logging()

    parser = argparse.ArgumentParser(description="Detect and measure bubbles from an image.")
    parser.add_argument("image_path", type=str, help="Path to the image file.")
    args = parser.parse_args()

    detect_bubbles(args.image_path)
