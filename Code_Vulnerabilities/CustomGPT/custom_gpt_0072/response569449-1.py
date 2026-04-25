
from Bio import Entrez

# Set your email
Entrez.email = "your_email@example.com"

# Function to get taxonomy and organelle
def fetch_taxonomy_and_organelle(accession):
    # Fetch the GenBank record
    handle = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text')

    # Read the GenBank record
    record = handle.read()

    # Check for organelle and taxonomy
    organelle = None
    taxonomy = None

    if "ORG" in record:
        # Extract organelle
        start = record.index("ORG")
        end = record.index("\n", start)
        organelle = record[start:end].split(' ')[1:]  # Organelles are usually listed

    if "taxonomy" in record:
        # Extract taxonomy
        for line in record.splitlines():
            if line.startswith("taxonomy"):
                taxonomy = line.split()[1:]  # Split and get taxonomy

    return organelle, taxonomy

# Example usage
accession_id = "YOUR_ACCESSION_NUMBER_HERE"
organelle, taxonomy = fetch_taxonomy_and_organelle(accession_id)

print("Organelle:", organelle)
print("Taxonomy:", taxonomy)
