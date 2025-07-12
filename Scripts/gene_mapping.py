from Bio import Entrez

Entrez.email = "swaroopbhat2003@gmail.com"


output_file = open("protein_gene_mapping_2000.txt", "w")
output_file.write("Gene Name\tProtein\n")

with open("protein_2000.txt", "r") as file:
    for line in file:
        protein_name = line.strip()
        
        if not protein_name:  
            continue
        
        query = f"{protein_name}[organism=Klebsiella pneumoniae]"
        search_handle = Entrez.esearch(db="protein", term=query, retmax=1)
        search_results = Entrez.read(search_handle)
        search_handle.close()
        
        if search_results["IdList"]:
            protein_id = search_results["IdList"][0]  
            
            fetch_handle = Entrez.efetch(db="protein", id=protein_id, rettype="gb", retmode="text")
            record = fetch_handle.read()
            fetch_handle.close()
            
            gene_name = "Unknown"
            for line in record.split("\n"):
                if "/gene=" in line:
                    gene_name = line.split("=")[1].replace('"', '').strip()
                    break
            
            print(f"{gene_name} -> {protein_name}")  
            output_file.write(f"{gene_name}\t{protein_name}\n")  
            
        else:
            print(f"No match found for: {protein_name}")
            output_file.write(f"{protein_name}\tNot Found\n")  

output_file.close()
print("Results saved in protein_gene_mapping.txt")



