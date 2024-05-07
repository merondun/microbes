#!/bin/bash

#SBATCH --get-user-env
#SBATCH --mail-user=merondun@bio.lmu.de
#SBATCH --clusters=cm2_tiny
#SBATCH --partition=cm2_tiny
#SBATCH --cpus-per-task=5
#SBATCH --time=6:00:00

metadb=/dss/dsslegfs01/pr53da/pr53da-dss-0021/projects/2021__Cuckoo_Resequencing/tmp/meta_db

mkdir profiles
cd /dss/dsshome1/lxc07/di39dux/microbe/filtered_fastq/merged_reads

for ID in $(cat IDS.list); do

metaphlan ${ID}_R1.concat.fastq,${ID}_R2.concat.fastq --bowtie2out profiles/${ID} --unclassified_estimation --bowtie2db ${metadb} --input_type fastq --nproc 5 > profiles/${ID}_profile.txt

done
