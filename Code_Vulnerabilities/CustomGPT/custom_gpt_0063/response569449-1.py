
from Bio import SeqIO
from Bio import Entrez

Entrez.email = "your_email@example.com"  # Always include your email in Entrez requests

def fetch_genbank_info(accession):
    # Use efetch to get the GenBank record
    with Entrez.efetch(db='nucleotide', id=accession, rettype='gbwithparts', retmode='text') as gb_file:
        record = SeqIO.read(gb_file, 'genbank')

    # Access the desired features
    taxonomy = record.annotations.get('taxonomy', [])
    organelle = None

    for feature in record.features:
        if 'organelle' in feature.qualifiers:
            organelle = feature.qualifiers['organelle'][0]

    return taxonomy, organelle

# Example usage
accession_numbers = ["NC_001301", "NC_002695"]  # Replace with your actual accession numbers
for accession in accession_numbers:
    taxonomy, organelle = fetch_genbank_info(accession)
    if taxonomy and taxonomy[1] == 'Fungi':
        print(f"{accession} is a fungi with organelle: {organelle}")
