#!/bin/bash

# Define the parent directory containing Prokka output folders
parent_dir="home/swaroop/ST307_annotation_data"

# Define the target directory to store all .faa files
output_dir="$parent_dir/merged_faa"

# Create the target directory if it doesn't exist
mkdir -p "$output_dir"

# Loop through each subdirectory inside parent_dir
for folder in "$parent_dir"/*/; do
    # Find the .faa file inside the current folder
    faa_file=$(find "$folder" -maxdepth 1 -type f -name "*.faa")

    # Check if a .faa file exists in the current folder
    if [[ -n "$faa_file" ]]; then
        # Get the folder name (basename) to ensure uniqueness
        folder_name=$(basename "$folder")
        destination_file="$output_dir/${folder_name}.faa"

        # Copy and rename the .faa file to prevent overwriting
        cp "$faa_file" "$destination_file"

        echo "Copied: $faa_file -> $destination_file"
    fi
done

# Final message
echo "All .faa files have been copied to $output_dir."

