
from Bio import Entrez

# Make sure to set your email as per NCBI's requirements
Entrez.email = "your_email@example.com"

def fetch_taxonomy_and_organelle(accession):
    handle = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text')

    # Read the GenBank record line by line
    for line in handle:
        # Check for taxonomy
        if line.startswith('  ORGANISM'):
            organism = line.strip().split(' ', 1)[1]  # Get the organism name
            print("Organism:", organism)

        elif line.startswith('     organelle'):
            organelle = line.strip().split(' ', 1)[1]  # Get the organelle name
            print("Organelle:", organelle)

    handle.close()

# Example usage
fetch_taxonomy_and_organelle("YOUR_ACCESSION_NUMBER")
