Intestinal metagenomics

Leveraging 18 libraries, encompassing 3 samples, 2 locations, and 3 replicates, answering this:

**Broad questions:**

* Are any microbes biopsy-specific? 
* Do biopsies have high microbial community overlap, or are there tissue-specific communities?

**Specific questions:**

1. How was the sequencing run? Anything to change if we could go back in time?
2. What taxonomic groups are present in the samples?
3. Which samples contain microbes that can produce colibactin?
4. Do some exploratory data analysis. Make some figures and do some stats and relate it back to the broad questions. 


## Directory Structure

### `/raw_fastq`

Contains the [tiny] raw FASTQ files, as well as multiQC outputs from the R1 and R2 splits, and MetaPhlAn on the unfiltered reads. 

### `/read_counts`

Counts of reads per sample across filters from raw data all the way to trimmed and decontaminated. 

### `/trimmed_fastq`

Output from knead_data, many fastq files. 

### `/species_profiling`

Includes results from microbial community profiling. Files from MetaPhlAn at both the technical replicate level and the biological replicate level. 

### `/genomes`

Using the species identified from the MetaPhlAn analyses, download their genomes and see if they contain the [clb](https://www.science.org/doi/10.1126/science.1127059?url_ver=Z39.88-2003&rfr_id=ori:rid:crossref.org&rfr_dat=cr_pub%20%200pubmed) gene cluster which is diagnostic of colibactin producing bacteria. 

## Authors

- **Justin Merondun** - [merondun](https://github.com/merondun/). [Website](https://justinmerondun.wordpress.com/). Contact: heritabilities [at] gmail.com 
