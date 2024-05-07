# Trimmed and decontaminated data, after knead_data processing

Many individual fastq files corresponding to the filters.

Files:

- `*trimmed*`: files trimmed, but no decontam yet 
- `*repeats.removed*`: trimmed and repeats removed using `trf`
- `*unmatched_contam*`: sequences unmatched to contam, empty in all cases here
- `*paired_contam*`: contaminants or host DNA from human
- `*kneaddata_paired*`: final microbe data trimmed, repeatless, and without host or contaminant DNA 

Directories: 

- `multiqc_report`: report from multiQC on final trimmed and cleaned data. Temporary individual fastQC files were deleted to save space 
