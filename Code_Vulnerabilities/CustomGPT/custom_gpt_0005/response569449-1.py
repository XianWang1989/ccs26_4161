
from Bio import Entrez

# Function to get organelle and taxonomy
def fetch_taxonomy_and_organelle(accession):
    Entrez.email = "your_email@example.com"  # Always provide your email
    handle = Entrez.efetch(db="nucleotide", id=accession, rettype="gb", retmode="text")

    # Read through the GenBank file line by line
    for line in handle:
        # Check for taxonomy in annotations
        if line.startswith("     ORGANISM"):
            organism = line.split(' ')[2].strip()
        if "taxonomy" in line:
            taxonomy = line.split("=")[1].strip().strip('"')

        # Find organelle information
        if "organelle" in line:
            organelle = line.split("=")[1].strip().strip('"')

    handle.close()
    return taxonomy, organelle

# Example usage
access1 = "YOUR_ACCESSION_NUMBER"
taxonomy, organelle = fetch_taxonomy_and_organelle(access1)

print(f"Taxonomy: {taxonomy}, Organelle: {organelle}")
