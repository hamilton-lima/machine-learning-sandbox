#!/bin/bash

# Loop through each .PNG file in the current directory
for file in *.PNG; do
    # Check if the file exists to avoid errors
    if [ -f "$file" ]; then
        # Extract the filename without the extension
        base=${file%.PNG}
        # Rename the file to .ong
        mv "$file" "${base}.png"
    fi
done
