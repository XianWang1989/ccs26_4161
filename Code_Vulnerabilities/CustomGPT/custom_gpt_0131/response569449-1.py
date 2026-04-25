
from Bio import Entrez

# Function to fetch taxonomy and organelle information
def fetch_taxonomy_organelle(accession):
    # Fetch GenBank data
    handle = Entrez.efetch(db="nucleotide", id=accession, rettype="gb", retmode="text")
    # Read and parse the content of the GenBank record
    record = handle.read()

    # Look for taxonomy in the record
    taxonomy = None
    organelle = None

    # Process the record to extract only the required features
    # Check for taxonomy
    if "taxonomy" in record:
        start_tax = record.index("taxonomy") + len("taxonomy") + 1
        end_tax = record.index("\n", start_tax)
        taxonomy = record[start_tax:end_tax].strip()

    # Check for organelle
    if "organelle" in record:
        start_org = record.index("organelle") + len("organelle") + 1
        end_org = record.index("\n", start_org)
        organelle = record[start_org:end_org].strip()

    return taxonomy, organelle

# Usage example
accession_number = "YOUR_ACCESSION_NUMBER_HERE"
taxonomy, organelle = fetch_taxonomy_organelle(accession_number)

print(f"Taxonomy: {taxonomy}")
print(f"Organelle: {organelle}")
