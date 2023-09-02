import cv2
import numpy as np
import logging
import argparse
import os
from datetime import datetime

def setup_logging():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s]: %(message)s")

def detect_bubbles(image_path):
    logging.info("Starting bubble detection.")

    # Read the image
    logging.info(f"Reading image from {image_path}.")
    img = cv2.imread(image_path, cv2.IMREAD_COLOR)

    # Convert the image to grayscale
    logging.info("Converting image to grayscale.")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Threshold the image to binary
    logging.info("Applying binary thresholding.")
    _, thresh = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)

    # Find contours
    logging.info("Finding contours.")
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    bubble_sizes = []

    for contour in contours:
        # Skip small contours that are not likely to be bubbles
        if cv2.contourArea(contour) < 50:
            continue

        # Fit a circle to the contour and draw it
        ((x, y), radius) = cv2.minEnclosingCircle(contour)
        cv2.circle(img, (int(x), int(y)), int(radius), (0, 255, 0), 2)

        # Record the bubble size (radius)
        bubble_sizes.append(radius)

        logging.info(f"Radius of detected bubble: {radius}")
        logging.info(f"Diameter of detected bubble: {2*radius}")

    # Save the output image
    result_folder = "result"
    if not os.path.exists(result_folder):
        logging.info("Creating result folder.")
        os.makedirs(result_folder)

    # Extract the original file name (without extension) from the image_path
    original_file_name = os.path.splitext(os.path.basename(image_path))[0]
    
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    output_filename = f"{result_folder}/detect-test2-{original_file_name}-{timestamp}.jpg"
    
    logging.info(f"Saving the output image to {output_filename}.")
    cv2.imwrite(output_filename, img)

    logging.info("Bubble detection completed.")
    return bubble_sizes

if __name__ == "__main__":
    setup_logging()

    parser = argparse.ArgumentParser(description="Detect and measure bubbles from an image.")
    parser.add_argument("image_path", type=str, help="Path to the image file.")
    args = parser.parse_args()

    detect_bubbles(args.image_path)
