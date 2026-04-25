
from Bio import Entrez
from Bio import SeqIO

# Function to fetch essential data from GenBank using accession number
def fetch_genbank_metadata(accession):
    # Fetch GenBank record
    with Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text') as handle:
        record = SeqIO.read(handle, 'genbank')

    # Extract taxonomy and organelle features
    taxonomy = record.annotations.get('taxonomy', [])
    organelle = None

    # Look for organelle in features
    for feature in record.features:
        if 'organelle' in feature.qualifiers:
            organelle = feature.qualifiers['organelle']
            break

    return taxonomy, organelle

# Example usage
Entrez.email = "your_email@example.com"  # Always include your email
accession = "YOUR_ACCESSION_NUMBER_HERE"  # Replace with actual accession number
taxonomy, organelle = fetch_genbank_metadata(accession)

# Output results
print(f"Taxonomy: {taxonomy}")
print(f"Organelle: {organelle}")
