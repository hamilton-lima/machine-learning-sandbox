import os
import shutil
import json

def move_and_rename_files(source_folder, target_folder):
    # Create the target folder if it doesn't exist
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    moved_files_info = []

    # Traverse through the subfolders and move files
    for root, _, files in os.walk(source_folder):
        for filename in files:
            source_file_path = os.path.join(root, filename)

            # Get the subfolder name
            subfolder_name = os.path.basename(root)

            # New filename with subfolder prefix
            new_filename = f"{subfolder_name}_{filename}"

            # Path to the target file
            target_file_path = os.path.join(target_folder, new_filename)

            # Move and rename the file
            shutil.move(source_file_path, target_file_path)

            # Record moved file info
            moved_file_info = {
                "original_subfolder": subfolder_name,
                "original_filename": filename,
                "new_filename": new_filename
            }
            moved_files_info.append(moved_file_info)

    # Write moved files info to a JSON file
    json_filename = os.path.join(target_folder, "moved_files_info.json")
    with open(json_filename, "w") as json_file:
        json.dump(moved_files_info, json_file, indent=4)

if __name__ == "__main__":
    source_folder = "original-test-data"
    target_folder = "test-data"

    move_and_rename_files(source_folder, target_folder)
