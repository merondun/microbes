#!/bin/bash

#SBATCH --get-user-env
#SBATCH --mail-user=merondun@bio.lmu.de
#SBATCH --clusters=cm2_tiny
#SBATCH --partition=cm2_tiny
#SBATCH --cpus-per-task=2
#SBATCH --time=6:00:00

metadb=/dss/dsslegfs01/pr53da/pr53da-dss-0021/projects/2021__Cuckoo_Resequencing/tmp/meta_db

cd /dss/dsshome1/lxc07/di39dux/microbe/filtered_fastq/merged_reads

for ID in $(cat IDS.list); do 

echo "Working on sample: ${ID}"

humann --input ${ID}.bothreads_concat.fastq --taxonomic-profile profiles/${ID}_profile.txt --output humann

done
