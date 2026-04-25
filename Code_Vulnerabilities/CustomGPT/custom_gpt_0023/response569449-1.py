
from Bio import Entrez

# Function to fetch only taxonomy and organelle information
def fetch_taxonomy_and_organelle(accession):
    Entrez.email = "your_email@example.com"  # Always include your email
    with Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text') as handle:
        for line in handle:
            if line.startswith("   taxonomy"):
                taxonomy = line.strip().split("   ")[-1]  # Extract taxonomy line
                break
        else:
            taxonomy = None

        organelle = None
        for line in handle:
            if line.startswith("     organelle"):
                organelle = line.strip().split("   ")[-1]  # Extract organelle line
                break

    return taxonomy, organelle

# Example usage
accession = "YOUR_ACCESSION_NUMBER"
taxonomy, organelle = fetch_taxonomy_and_organelle(accession)

if taxonomy:
    print(f"Taxonomy: {taxonomy}")
if organelle:
    print(f"Organelle: {organelle}")
