
from Bio import SeqIO
from Bio import Entrez

# Function to fetch taxonomy and organelle information
def fetch_taxonomy_organelle(accession):
    # Fetch GenBank record
    handle = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text')
    record = SeqIO.read(handle, 'genbank')
    handle.close()

    # Extract taxonomy
    taxonomy = record.annotations.get('taxonomy', [])
    organelle = None

    # Check for organelle feature
    for feature in record.features:
        if 'organelle' in feature.qualifiers:
            organelle = feature.qualifiers['organelle'][0]  # Get the first organelle
            break

    return taxonomy, organelle

# Example usage
accession = 'YOUR_ACCESSION_NUMBER'  # Replace with your accession number
taxonomy, organelle = fetch_taxonomy_organelle(accession)

if 'Fungi' in taxonomy:
    print(f'Accession {accession} belongs to Fungi.')
if organelle:
    print(f'Organelle: {organelle}')
