import cv2
import numpy as np
import argparse
import os
import logging

def setup_logging():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def save_image(image, filename_prefix, image_path):
    filename = os.path.basename(image_path)
    output_path = os.path.join('result', f"{filename_prefix}_{filename}")
    cv2.imwrite(output_path, image)
    logging.info(f"Image saved at stage: {filename_prefix} as {output_path}")

def main(image_path):
    # Create the 'result' folder if it doesn't exist
    logging.info("Checking if 'result' folder exists.")
    if not os.path.exists('result'):
        os.makedirs('result')
        logging.info("'result' folder created.")
    
    logging.info(f"Reading image from {image_path}.")
    image = cv2.imread(image_path)
    save_image(image, 'original', image_path)

    if image is None:
        logging.error("Could not open the image file.")
        return
    
    logging.info("Converting image to grayscale.")
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    save_image(gray_image, 'gray', image_path)
    
    logging.info("Applying GaussianBlur.")
    blurred_image = cv2.GaussianBlur(gray_image, (15, 15), 0)
    save_image(blurred_image, 'blurred', image_path)
    
    logging.info("Detecting circles using HoughCircles.")
    circles = cv2.HoughCircles(blurred_image, cv2.HOUGH_GRADIENT, 1, minDist=40, param1=50, param2=30, minRadius=5, maxRadius=250)

    if circles is not None:
        logging.info("Circles detected. Drawing circles.")
        circles_image = np.copy(image)
        circles = np.round(circles[0, :]).astype("int")
        for (x, y, r) in circles:
            cv2.circle(circles_image, (x, y), r, (0, 255, 0), 4)
        save_image(circles_image, 'circles', image_path)
    else:
        logging.info("No circles detected.")
    
    logging.info("Finding contours.")
    ret, thresh = cv2.threshold(blurred_image, 50, 255, 0)
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    logging.info("Drawing contours.")
    contours_image = np.copy(image)
    cv2.drawContours(contours_image, contours, -1, (0, 0, 255), 2)
    save_image(contours_image, 'contours', image_path)
    
    logging.info("Saving the final output image.")
    filename = os.path.basename(image_path)
    output_path = os.path.join('result', 'final_' + filename)
    cv2.imwrite(output_path, image)
    logging.info(f"Result image saved as {output_path}")

if __name__ == "__main__":
    setup_logging()
    parser = argparse.ArgumentParser(description='Draw contours and circles on an image.')
    parser.add_argument('image_path', help='Path to the image file.')
    
    args = parser.parse_args()
    main(args.image_path)
