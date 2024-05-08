# Genome approaches for assessing colibactin production 

Profiles for metaphlam outputs, bowtie databases deleted for space. Blastdbs were deleted to save space.

Files:

- `Species.list`: List of species identified across all potential metaphlan profiles 
- `Primers.fa`: Forward and reverse primers for clb genes from https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7065307/
- `antismash_gene_clusters.txt`: output of pathways identified from antismash


Directories:

- `fasta`: RefSeq assemblies for each candidate species
- `antismash`: Species-specific results from antismash, zip folders contain an html report
- `blasted`: blast results, blasting Primers.fa against each reference genome. 
