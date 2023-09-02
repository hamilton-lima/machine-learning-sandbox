import cv2
import os
import time
import glob

def capture_camera_stream(camera_url, camera_name, save_interval=1, retain_duration=300):
    output_folder = f"last 5 minutes {camera_name}"
    
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Open the camera stream
    cap = cv2.VideoCapture(camera_url)
    
    if not cap.isOpened():
        print(f"Error: Cannot open camera stream {camera_url}")
        return
    
    frame_count = 0
    last_saved_time = 0

    try:
        while True:
            current_time = int(time.time())
            
            # Read a frame from the camera stream
            ret, frame = cap.read()
    
            # If we can't read a frame, break the loop
            if not ret:
                break
            
            # If it is time to save a new frame
            if current_time - last_saved_time >= save_interval:
                # Construct the output image path
                timestamp = current_time
                output_path = os.path.join(output_folder, f"frame_{timestamp}.jpg")
    
                # Save the frame as an image
                cv2.imwrite(output_path, frame)
                
                last_saved_time = current_time
                
                # Remove files that are older than retain_duration seconds
                for old_file in glob.glob(f"{output_folder}/frame_*.jpg"):
                    file_timestamp = int(old_file.split('_')[-1].split('.')[0])
                    if current_time - file_timestamp > retain_duration:
                        os.remove(old_file)
                
                frame_count += 1
                print(f"Saved frame {frame_count}")

    except KeyboardInterrupt:
        print("Exiting...")
    
    finally:
        # Release the video capture object
        cap.release()

if __name__ == "__main__":
    camera_url = "http://localhost:8080/camera"  # Replace with your camera URL or ID. '0' will access the default camera
    camera_name = "Camera1"  # Replace with the name of your camera
    capture_camera_stream(camera_url, camera_name)
