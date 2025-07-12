```markdown
#  Investigating *Klebsiella pneumoniae* ST307: Genome Annotation and PPI Network Insights

This repository documents a computational biology project aimed at discovering possible therapeutic targets in *Klebsiella pneumoniae* ST307 — a multidrug-resistant (MDR) lineage that has rapidly become a threat in healthcare environments globally.

By integrating genome annotation and protein-protein interaction (PPI) analysis, this study narrows down essential genes that could serve as druggable targets.

---

##  Summary of Approach

The workflow involved several key steps:

1. **Genome Collection**  
   Retrieved ~1500 *K. pneumoniae* ST307 genome assemblies from the NCBI database.

2. **Quality Control**  
   Performed initial assessment using **FastQC** and **QUAST** to evaluate sequence quality.

3. **Genome Filtering**  
   Selected 886 high-quality genome assemblies for downstream analysis.

4. **Functional Annotation**  
   Annotated genomes with **Prokka**, yielding approximately 450,000 protein sequences.

5. **Protein Selection**  
   Excluded hypothetical and redundant proteins, resulting in 3,920 unique protein sequences.

6. **PPI Network Construction**  
   Used the **STRING database** to predict protein-protein interactions.

7. **Network Analysis**  
   Visualized and analyzed the network in **Cytoscape**, using the **cytoHubba** plugin to identify central nodes based on:
   - Degree
   - MCC (Maximal Clique Centrality)
   - DMNC (Density of Maximum Neighborhood Component)
   - Bottleneck
   - Closeness centrality

8. **Hub Gene Identification**  
   Cross-referenced top-ranking proteins across all metrics to finalize **six key candidate genes**.

---

##  Final Candidate Genes

The following six genes were identified as potential therapeutic targets due to their essential roles in cellular function and stress adaptation:

```
prsA   metG   pheT   guaA   arcB   smpB
```

These genes are involved in critical metabolic and regulatory processes within the bacterium.

---

##  Tools and Technologies Used

- **Quality Control:** FastQC, QUAST  
- **Annotation:** Prokka  
- **Scripting and Parsing:** Python (Pandas), Bash  
- **PPI Data Source:** STRING Database  
- **Network Visualization & Analysis:** Cytoscape, cytoHubba  
- **Data Handling & Plotting:** Excel, Matplotlib

---

##  What’s Next?

This study lays the groundwork for future research avenues, including:

- **Druggability analysis** of the hub proteins  
- **Structure-based virtual screening** to identify inhibitory compounds  
- **Molecular dynamics simulations** for target validation  
- **Comparative genomics** with other *K. pneumoniae* lineages  
- **Experimental (wet-lab) validation** to confirm computational predictions

These efforts aim to accelerate the discovery of novel therapies against MDR *K. pneumoniae* ST307.

---

##  Reproducing the Environment

To replicate the analysis environment, use the included `prokka_env.yml` file:

```bash
conda env create -f prokka_env.yml
conda activate prokka_env
```

---

##  Contact & Collaboration

For questions, suggestions, or collaboration opportunities, feel free to reach out:

- **Name:** Swaroop Bhat  
- **Email:** swaroopbhat25@gmail.com  
- **GitHub:** [github.com/swaroop1414](https://github.com/swaroop1414)
```
