# Read count summaries

Read counts across different filters, from raw to trimmed and decontaminated

Files:

- `Read_Counts.txt`: seqkit output of read length, from `seqkit stats * | sed 's/,//g' > Read_Counts.txt` when all fastq files are in one directory
- `Summarize_Counts.py`: script to format the `Read_Counts.txt` nicely for R. It requires a few positional arguments 

**INPUTS:**

* `--out` output summary
* Positional argument of `Read_Counts.txt`

- `Read_Counts_Output.txt`: output from script. e.g.:

```
head Read_Counts_Output.txt
ID      Location        Replicate       Filter  num_seqs        sum_len avg_len Read_pair
P1      Ileum   1       Raw     27648   2792448 101.0   1
P1      Ileum   1       Contaminants    4498    268882  59.8    1
P1      Ileum   1       Contaminants    4498    268882  59.8    1
P1      Ileum   1       Dropped 0       0               1
P1      Ileum   1       Dropped 0       0               1
```

