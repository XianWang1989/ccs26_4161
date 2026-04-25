
from Bio import Entrez
import json

# Function to fetch taxonomy and organelle information
def fetch_taxonomy_and_organelle(accession):
    # Fetch the GenBank record using Entrez
    handle = Entrez.efetch(
        db='nucleotide',
        id=accession,
        rettype='gb',
        retmode='text'
    )

    # Read the record
    record = handle.read()
    handle.close()

    # Extract taxonomy information
    # The taxonomy is usually in the annotations section
    lines = record.splitlines()
    taxonomy = None
    organelle = None

    for line in lines:
        if line.startswith('ORGANISM'):
            organelle = line.split(' ')[1:]  # Adjust based on actual format
        if 'taxonomy' in line:
            taxonomy = line.split('taxonomy: ')[1]  # Adjust based on actual output format

    return {
        'taxonomy': taxonomy,
        'organelle': organelle
    }

# Example usage
accessions = ['ACCESSION_1', 'ACCESSION_2']  # Replace with your accession numbers
results = {}

for acc in accessions:
    results[acc] = fetch_taxonomy_and_organelle(acc)

# Display results
print(json.dumps(results, indent=2))
