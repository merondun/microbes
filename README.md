# Intestinal metagenomics

Leveraging 18 libraries, encompassing 3 samples, 2 locations, and 3 replicates, answering this:

**Broad questions:**

* Are any microbes biopsy-specific? 
* Do biopsies have high microbial community overlap, or are there tissue-specific communities?

**Specific questions:**

1. How was the sequencing run? Anything to change if we could go back in time?
2. What taxonomic groups are present in the samples?
3. Which samples contain microbes that can produce colibactin?
4. Do some exploratory data analysis. Make some figures and do some stats and relate it back to the broad questions. 


## Report

Metagenomics has provided valuable insights into the differences in microbial species along the gastrointestinal (GI) tract and their role in various health conditions, including cancer and liver disease (Delik et al., 2022; Kharofa et al., 2023; Mannion et al., 2023). While many microbiome studies rely on 16S rRNA gene sequencing or fecal sampling for accessibility, the use of shotgun metagenomics offers a genome-resolved understanding of microbial communities directly from tissue biopsies (Cheng et al., 2022). Here, I briefly analyze shotgun reads from rectum and terminal ileum biopsies in three patients, potentially enriched using microbial-enrichment methods (Wu-Woods et al., 2023), to identify any biopsy-specific microbial species capable of producing colibactin, a genotoxic molecule implicated in cancer (Vizcaino & Crawford, 2015). 

**Methods**

*Quality control*

A total of 18 libraries were analyzed, encompassing three patients, two tissues (rectum, terminal ileum), and three replicates. Interleaved paired-end reads were separated into forward and reverse files and analyzed independently with FastQC v0.12.1 (Andrews, 2010) and compiled using MultiQC v1.19 (Ewels et al., 2016). Reads were filtered using Knead Data v0.12.0 with default settings, which trims reads using trimmomatic v0.39 (Bolger et al., 2014), removes repeats with trf v4.09 (Benson, 1999), and identifies host (human) and common contaminants. Processed reads were then processed with FastQC and MultiQC. Reads counts from raw and filtered steps were summarized with python and visualized in R v4.3.2 with the tidyverse v2.0.0 (R Core Team, 2017; Wickham et al., 2019). 

*Community profiling*

Filtered metagenomic reads were analyzed with MetaPhlAn v4.1.0 (Blanco-Miguez et al., 2022) and visualized with hclust2 (https://github.com/SegataLab/hclust2). Profiling was performed on three data subsets to assess sensitivity and overlap of species across various filters: 1) filtered reads at the technical replicate level (*n* = 18 samples); 2) filtered reads merged at the biological replicate level (*n =* 6 samples); 3) raw unfiltered reads merged at the biological replicate level (*n =* 6 samples). 

*Microbial species producing colibactin*

All potential microbial species identified from community profiling were investigated to determine if they were capable of producing colibactin. Colibactin was first identified as being produced by *Escherichia coli*, leveraging a 54-kb gene cluster (Nougayrède et al., 2006), with additional evidence identifying this gene cluster across broader taxa (Kawanishi et al., 2020). I used two approaches to determine if any of our candidate species harbor genes in the NRPS and PKS enzymatic pathway involved with colibactin production (Nougayrède et al., 2006). First, I downloaded all RefSeq whole genomes for each candidate species and blasted the 64 *clb* gene primers against each genome using BLASTn v2.15.0+ (Camacho et al., 2009). Based on interspecific distance I used a relaxed word size of 15 and an evalue of 0.05. Secondly, I used antismash v7.1.0 (Blin et al., 2021) to predict secondary metabolite biosynthesis gene clusters using the RefSeq genomes, using prodigal for prediction (Hyatt et al., 2010). Pathways were extracted from each run and summarized in R. 

**Results & Discussion**

Sequencing runs were somewhat successful despite high adapter content, overrepresented ‘GGGG...’ sequences, and highly fragmented libraries (Fig. 1). The initial 10 bases of the reads exhibited strange base composition, potentially from library preparation protocols. Quality control sufficiently ameliorated adapter and overrepresented sequence issues (Fig. 1). Overall, output per library was highly variable, making biological inference suspect due to variable amount of sequence across biological replicates (Figs. S1 & S2). 

A maximum of 11 microbial species were identified across the libraries, with only five of those species identified across both technical and biological replicates (Fig. 2). Only a single individual (P2) exhibited consistent microbial communities, indicating that this sample was likely a target of microbial enrichment, while the remaining two individuals (P1 and P3) were not. Within individual P2, the species *Mediterraneibacter faecis, Dialister invisus,* and *Bacteroides uniformis* were only identified in the terminal ileum, while only *Ruminococcus bromii* was identified in the rectum. *Alistipes putredinis, Phocaeicola vulgatus*, and *Akkermansia municiphila* were found in both biopsies. Only one of these species was identified as potential colibactin-producing candidates, including *Ruminococcus bromii* in the rectum (Fig. 3). While *Phocaeicola massiliensis* was identified as a potential colibactin-producing candidate from the profiles using raw and unfiltered reads, only *Ruminococcus bromii* was identified from filtered reads (Fig. 2). 

Future bioinformatic directions could assess specific gene pathways within the sequenced reads themselves using HuManN, assemble metagenome-assembled genomes if provided with additional reads using anvi’o, or replicate analyses with QIIME2. Overall, additional reads are required across replicates to ensure biological reproducibility.

 **References**

Andrews, S. (2010). FastQC: A quality control tool for high throughput sequence data. Available at https://www.bioinformatics.babraham.ac.uk/projects/fastqc/ (p. Online) [Computer software].

Benson, G. (1999). Tandem repeats finder: A program to analyze DNA sequences. Nucleic Acids Research, 27(2), 573–580. https://doi.org/10.1093/nar/27.2.573

Blanco-Miguez, A., Beghini, F., Cumbo, F., McIver, L. J., Thompson, K. N., Zolfo, M., Manghi, P., Dubois, L., Huang, K. D., Thomas, A. M., Piccinno, G., Piperni, E., Punčochář, M., Valles-Colomer, M., Tett, A., Giordano, F., Davies, R., Wolf, J., Berry, S. E., … Segata, N. (2022). Extending and improving metagenomic taxonomic profiling with uncharacterized species with MetaPhlAn 4. https://doi.org/10.1101/2022.08.22.504593

Blin, K., Shaw, S., Kloosterman, A. M., Charlop-Powers, Z., van Wezel, G. P., Medema, M. H., & Weber, T. (2021). antiSMASH 6.0: Improving cluster detection and comparison capabilities. Nucleic Acids Research, 49(W1), W29–W35. https://doi.org/10.1093/nar/gkab335

Bolger, A. M., Lohse, M., & Usadel, B. (2014). Trimmomatic: A flexible trimmer for Illumina sequence data. Bioinformatics, 30(15), 2114–2120. https://doi.org/10.1093/bioinformatics/btu170

Camacho, C., Coulouris, G., Avagyan, V., Ma, N., Papadopoulos, J., Bealer, K., & Madden, T. L. (2009). BLAST+: Architecture and applications. BMC Bioinformatics, 10(1), 421. https://doi.org/10.1186/1471-2105-10-421

Cheng, W. Y., Liu, W.-X., Ding, Y., Wang, G., Shi, Y., Chu, E. S. H., Wong, S., Sung, J. J. Y., & Yu, J. (2022). High Sensitivity of Shotgun Metagenomic Sequencing in Colon Tissue Biopsy by Host DNA Depletion. Genomics, Proteomics & Bioinformatics, S167202292200119X. https://doi.org/10.1016/j.gpb.2022.09.003

Delik, A., Dinçer, S., Ülger, Y., Akkız, H., & Karaoğullarından, Ü. (2022). Metagenomic identification of gut microbiota distribution on the colonic mucosal biopsy samples in patients with non-alcoholic fatty liver disease. Gene, 833, 146587. https://doi.org/10.1016/j.gene.2022.146587

Ewels, P., Magnusson, M., Lundin, S., & Käller, M. (2016). MultiQC: Summarize analysis results for multiple tools and samples in a single report. Bioinformatics, 32(19), 3047–3048. https://doi.org/10.1093/bioinformatics/btw354

Hyatt, D., Chen, G.-L., LoCascio, P. F., Land, M. L., Larimer, F. W., & Hauser, L. J. (2010). Prodigal: Prokaryotic gene recognition and translation initiation site identification. BMC Bioinformatics, 11(1), 119. https://doi.org/10.1186/1471-2105-11-119

Kawanishi, M., Shimohara, C., Oda, Y., Hisatomi, Y., Tsunematsu, Y., Sato, M., Hirayama, Y., Miyoshi, N., Iwashita, Y., Yoshikawa, Y., Sugimura, H., Mutoh, M., Ishikawa, H., Wakabayashi, K., Yagi, T., & Watanabe, K. (2020). Genotyping of a gene cluster for production of colibactin and in vitro genotoxicity analysis of Escherichia coli strains obtained from the Japan Collection of Microorganisms. Genes and Environment, 42(1), 12. https://doi.org/10.1186/s41021-020-00149-z

Kharofa, J., Haslam, D., Wilkinson, R., Weiss, A., Patel, S., Wang, K., Esslinger, H., Olowokure, O., Sohal, D., Wilson, G., Ahmad, S., & Apewokin, S. (2023). Analysis of the fecal metagenome in long‐term survivors of pancreas cancer. Cancer, 129(13), 1986–1994. https://doi.org/10.1002/cncr.34748

Mannion, A., Sheh, A., Shen, Z., Dzink-Fox, J., Piazuelo, M. B., Wilson, K. T., Peek, R., & Fox, J. G. (2023). Shotgun Metagenomics of Gastric Biopsies Reveals Compositional and Functional Microbiome Shifts in High- and Low-Gastric-Cancer-Risk Populations from Colombia, South America. Gut Microbes, 15(1), 2186677. https://doi.org/10.1080/19490976.2023.2186677

Nougayrède, J.-P., Homburg, S., Taieb, F., Boury, M., Brzuszkiewicz, E., Gottschalk, G., Buchrieser, C., Hacker, J., Dobrindt, U., & Oswald, E. (2006). Escherichia coli Induces DNA Double-Strand Breaks in Eukaryotic Cells. Science, 313(5788), 848–851. https://doi.org/10.1126/science.1127059

R Core Team. (2017). R: A language and environment for statistical computing. R Foundation for Statistical Computing, Vienna, Austria. URL https://www.R-project.org/. (p. Online) [Computer software].

Vizcaino, M. I., & Crawford, J. M. (2015). The colibactin warhead crosslinks DNA. Nature Chemistry, 7(5), 411–417. https://doi.org/10.1038/nchem.2221

Wickham, H., Averick, M., Bryan, J., Chang, W., McGowan, L., François, R., Grolemund, G., Hayes, A., Henry, L., Hester, J., Kuhn, M., Pedersen, T., Miller, E., Bache, S., Müller, K., Ooms, J., Robinson, D., Seidel, D., Spinu, V., … Yutani, H. (2019). Welcome to the Tidyverse. Journal of Open Source Software, 4(43), 1686. https://doi.org/10.21105/joss.01686

Wu-Woods, N. J., Barlow, J. T., Trigodet, F., Shaw, D. G., Romano, A. E., Jabri, B., Eren, A. M., & Ismagilov, R. F. (2023). Microbial-enrichment method enables high-throughput metagenomic characterization from host-rich samples. Nature Methods, 20(11), 1672–1682. https://doi.org/10.1038/s41592-023-02025-4

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
