#!/bin/bash

# Set the output directory
OUTPUT_DIR="home/swaroop/ST307_annotation"

# Create the output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

# Loop through each .fas file in the current directory
for fasta_file in *.fas; do
    if [[ -f "$fasta_file" ]]; then
        # Extract filename without extension
        base_name=$(basename "$fasta_file" .fas)

        # Run Prokka for each FASTA file
        prokka --outdir "$OUTPUT_DIR/$base_name" --prefix "$base_name" "$fasta_file"

        echo "Prokka annotation completed for: $fasta_file"
    else
        echo "File not found: $fasta_file"
    fi
done

echo "All files processed successfully!"

