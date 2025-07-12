input_file = "protein_names.txt"
output_file = "protein_names_filtered.txt"

with open(input_file, "r") as infile, open(output_file, "w") as outfile:
    for line in infile:
        if "hypothetical protein" not in line.strip().lower():
            outfile.write(line)
