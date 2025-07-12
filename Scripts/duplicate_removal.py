input_file = "protein_names_filtered.txt"
output_file = "protein_names_unique.txt"

seen = set()

with open(input_file, "r") as infile, open(output_file, "w") as outfile:
    for line in infile:
        protein = line.strip()
        if protein not in seen:
            seen.add(protein)
            outfile.write(protein + "\n")
