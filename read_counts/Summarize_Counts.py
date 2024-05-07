import argparse
import pandas as pd

def process_file(input_file, output_file):
    # Load data assuming tab-separated values and skipping potential whitespace
    df = pd.read_csv(input_file, sep='\s+', engine='python')
    
    # Parse the 'file' column to extract ID, Location, Replicate, and Read_pair
    df[['ID', 'Location', 'Replicate', 'Read_pair']] = df['file'].str.extract(r'(P\d+)_(Ileum|Rectum)_(\d+)_R(\d+)')
    
    # Define filter conditions based on 'file' content
    conditions = [
        (df['file'].str.contains('.gz')),
        (df['file'].str.contains('paired_contam')),
        (df['file'].str.contains('kneaddata_paired')),
        (df['file'].str.contains('repeats')),
        (df['file'].str.contains('trimmed')),
        (df['file'].str.contains('unmatched'))
    ]
    choices = ['Raw', 'Contaminants', 'Filtered', 'Repeatless', 'Trimmed', 'Dropped']
    df['Filter'] = pd.np.select(conditions, choices, default='Dropped')
    
    # Select and rename columns accordingly
    df = df[['ID', 'Location', 'Replicate', 'Filter', 'num_seqs', 'sum_len', 'avg_len', 'Read_pair']]
    
    # Output to a tab-separated file
    df.to_csv(output_file, sep='\t', index=False)

def main():
    parser = argparse.ArgumentParser(description="Process read count files.")
    parser.add_argument("input_file", help="Input file name")
    parser.add_argument("--out", dest="output_file", help="Output file name", required=True)
    
    args = parser.parse_args()
    
    # Process the file
    process_file(args.input_file, args.output_file)

if __name__ == "__main__":
    main()
