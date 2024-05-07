import sys
from Bio import Entrez
from Bio import SeqIO

def download_genome(species_name, output_dir):
    Entrez.email = "your.email@example.com"  # Set your email
    query = f"{species_name}[Orgn] AND refseq[Filter] AND complete genome[Filter]"
    search_handle = Entrez.esearch(db="nucleotide", term=query, retmax=10, sort="reldate")
    search_results = Entrez.read(search_handle)
    search_handle.close()

    if search_results["IdList"]:
        # Take the first ID, assumed to be the most recent
        accession_id = search_results["IdList"][0]
        fetch_handle = Entrez.efetch(db="nucleotide", id=accession_id, rettype="fasta", retmode="text")
        filename = f"{output_dir}/{species_name.replace(' ', '_')}_genome.fasta"

        with open(filename, "w") as out_handle:
            out_handle.write(fetch_handle.read())
        fetch_handle.close()
        print(f"Downloaded: {filename}")
    else:
        print(f"No recent complete RefSeq genome found for {species_name}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python download_genome.py <species_name> <output_directory>")
        sys.exit(1)

    species = sys.argv[1]
    output_directory = sys.argv[2]
    download_genome(species, output_directory)

