# Metaphlam community analyses

Re-named fastq files with "$PERSON_$LOCATION_$REPLICATE_$READ", and metaphlam analysis directly on technical replicates. Analysis repeated on combined at biological replicate level. 

Files:

- `Samples.list`: List of technical replicates
- `IDS.list`: List of biological replicates
- `Metaphlam.sh`: script to run metaphlam on technical replicates

Directories:

- `merged_reads`: reads concatenated into a single file, and associated metaphlam outputs
- `profiles`: metaplam outputs of technical replicates

