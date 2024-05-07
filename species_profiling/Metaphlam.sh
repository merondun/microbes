#!/bin/bash

#SBATCH --get-user-env
#SBATCH --mail-user=merondun@bio.lmu.de
#SBATCH --clusters=cm2_tiny
#SBATCH --partition=cm2_tiny
#SBATCH --cpus-per-task=5
#SBATCH --time=6:00:00

metadb=/dss/dsslegfs01/pr53da/pr53da-dss-0021/projects/2021__Cuckoo_Resequencing/tmp/meta_db

for SAMPLE in $(cat Samples.list); do 

metaphlan ${SAMPLE}_R1.fastq,${SAMPLE}_R2.fastq --bowtie2out profiles/${SAMPLE} --unclassified_estimation --bowtie2db ${metadb} --input_type fastq --nproc 5 > profiles/${SAMPLE}_profile.txt 

done
