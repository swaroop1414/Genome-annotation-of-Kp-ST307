import os
import glob

output_file = "protein_names.txt"

with open(output_file, "w") as outfile:
    for faa_file in glob.glob("*.faa"):
        with open(faa_file, "r") as infile:
            for line in infile:
                if line.startswith(">"):
                    parts = line.strip().split(None, 1)
                    if len(parts) > 1:
                        protein_name = parts[1]
                    else:
                        protein_name = "unknown"
                    outfile.write(protein_name + "\n")
