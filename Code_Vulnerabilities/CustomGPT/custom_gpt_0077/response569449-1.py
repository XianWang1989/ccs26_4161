
from Bio import Entrez

# Always set your email when using Entrez
Entrez.email = "your_email@example.com"

def fetch_taxonomy_and_organelle(accession):
    # Fetch the GenBank record
    with Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text') as gb_acc:
        gb_data = gb_acc.read()

    # Extract relevant information
    if "organism" in gb_data:
        # Extract organism name (around "ORGANISM" line)
        organism_line = [line for line in gb_data.splitlines() if line.startswith("ORGANISM")]
        organism = organism_line[0].split()[1] if organism_line else None

    if "taxonomy" in gb_data:
        # Extract taxonomy (around "taxonomy" annotation)
        taxonomy_start = gb_data.find("taxonomy")
        taxonomy_end = gb_data.find("\n", taxonomy_start)
        taxonomy = gb_data[taxonomy_start:taxonomy_end].strip().split()[1:]

    return organism, taxonomy

# Example usage
accession = "NC_001416"  # Replace with your accession number
organism, taxonomy = fetch_taxonomy_and_organelle(accession)
print(f"Organism: {organism}\nTaxonomy: {taxonomy}")
