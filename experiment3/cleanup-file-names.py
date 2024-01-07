import os
import re
import unicodedata


def clean_filename(filename):
    """Clean the file name, replacing extended characters with ASCII ones and spaces with underscores."""
    # Normalize the string to decompose extended characters
    normalized = unicodedata.normalize('NFD', filename)

    # Replace spaces with underscores
    normalized = normalized.replace(' ', '_')

    # Keep only ASCII characters
    cleaned = ''.join(c for c in normalized if unicodedata.category(
        c) != 'Mn' and c.isascii())

    return cleaned


def rename_files_in_directory(directory):
    """Rename files in the given directory and its subdirectories."""
    for root, dirs, files in os.walk(directory):
        for filename in files:
            clean_name = clean_filename(filename)
            if clean_name != filename:
                original_path = os.path.join(root, filename)
                new_path = os.path.join(root, clean_name)
                os.rename(original_path, new_path)
                print(f"Renamed '{original_path}' to '{new_path}'")


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python script.py <directory>")
        sys.exit(1)

    directory = sys.argv[1]
    if not os.path.isdir(directory):
        print(f"Error: '{directory}' is not a valid directory.")
        sys.exit(1)

    rename_files_in_directory(directory)
