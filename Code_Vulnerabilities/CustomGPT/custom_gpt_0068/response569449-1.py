
from Bio import Entrez
import re

Entrez.email = "your_email@example.com"  # Set your email here

def fetch_taxonomy_and_organelle(accession):
    # Fetch the GenBank data
    gb_data = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text').read()

    # Extract the taxonomy information
    taxonomy = re.search(r'\/taxonomy="(.+?)"', gb_data)
    organelle = re.search(r'\/organelle="(.+?)"', gb_data)

    taxonomy_value = taxonomy.group(1) if taxonomy else None
    organelle_value = organelle.group(1) if organelle else None

    return taxonomy_value, organelle_value

# Example usage
access1 = "YOUR_ACCESSION_NUMBER"  # Replace with your accession number
taxonomy, organelle = fetch_taxonomy_and_organelle(access1)

print(f"Taxonomy: {taxonomy}")
print(f"Organelle: {organelle}")
