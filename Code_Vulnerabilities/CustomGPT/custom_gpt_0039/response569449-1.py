
from Bio import Entrez

# Function to fetch specific features from GenBank
def fetch_genbank_features(accession):
    Entrez.email = "your.email@example.com"  # Always provide your email
    # Fetch the GenBank record
    handle = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text')

    # Read the record
    records = handle.read()

    # Extracting taxonomy and organelle information
    lines = records.splitlines()
    taxonomy = None
    organelle = None

    for line in lines:
        if line.startswith("                     /organism=\""):
            organelle = line.split("=")[1].strip("\"")
        if line.startswith("                    /taxonomy="):
            taxonomy = line.split("=")[1].strip()

    return taxonomy, organelle

# Example usage
accession_number = "YOUR_ACCESSION_NUMBER"
taxonomy, organelle = fetch_genbank_features(accession_number)

print(f"Taxonomy: {taxonomy}")
print(f"Organelle: {organelle}")
