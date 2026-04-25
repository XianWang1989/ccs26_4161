
from Bio import SeqIO
from Bio import Entrez

# Function to fetch specific GenBank information
def fetch_genbank_data(access_number):
    # Fetch the GenBank record
    gb_handle = Entrez.efetch(db='nucleotide', id=access_number, rettype='gb', retmode='text')
    record = SeqIO.read(gb_handle, 'genbank')

    # Initialize variables
    organelle = None
    taxonomy = []

    # Extract organelle if available
    for feature in record.features:
        if feature.type == 'source':
            organelle = feature.qualifiers.get('organelle', [''])[0]

    # Extract taxonomy if available
    taxonomy = record.annotations.get('taxonomy', [])

    return organelle, taxonomy

# Example usage
access1 = 'YOUR_ACCESSION_NUMBER'  # replace with your accession number
organelle, taxonomy = fetch_genbank_data(access1)
print(f'Organelle: {organelle}')
print(f'Taxonomy: {taxonomy}')
