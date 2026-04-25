
from Bio import Entrez
from Bio import SeqIO

Entrez.email = "your_email@example.com"  # Always provide your email

# Dictionary to cache the records
cache = {}

# Function to fetch only relevant features (taxonomy and organelle)
def fetch_genbank_partial(accession):
    # Fetch the GenBank file
    gb_file = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text')

    # Parse the GenBank record
    record = SeqIO.read(gb_file, 'genbank')
    # Cache the result
    cache[accession] = record

    # Extract taxonomy
    taxonomy = record.annotations.get('taxonomy', [])
    organelle = None

    # Looking for the organelle feature
    for feature in record.features:
        if 'organelle' in feature.qualifiers:
            organelle = feature.qualifiers['organelle'][0]

    return taxonomy, organelle

# Example usage
accession_number = 'YOUR_ACCESSION_NUMBER'  # Replace with your actual accession number
taxonomy, organelle = fetch_genbank_partial(accession_number)

if taxonomy and 'Fungi' in taxonomy:
    print("Fungi found in taxonomy")
if organelle:
    print(f"Organelle: {organelle}")
