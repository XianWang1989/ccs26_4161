
from Bio import Entrez
from Bio import SeqIO

# Setup your email (required by NCBI)
Entrez.email = "your_email@example.com"

# Function to get organelle and taxonomy
def get_organelle_and_taxonomy(access):
    # Fetch the GenBank record
    handle = Entrez.efetch(db='nucleotide', id=access, rettype='gb', retmode='text')
    record = SeqIO.read(handle, 'genbank')
    handle.close()

    # Initialize variables
    organelle = None
    taxonomy = None

    # Check for organelle in the features
    for feature in record.features:
        if feature.type == 'source' and 'organelle' in feature.qualifiers:
            organelle = feature.qualifiers['organelle'][0]

    # Get taxonomy
    if 'taxonomy' in record.annotations:
        taxonomy = record.annotations['taxonomy']

    return organelle, taxonomy

# Example accession number
access1 = 'YOUR_ACCESSION_NUMBER'
organelle, taxonomy = get_organelle_and_taxonomy(access1)

print(f'Organelle: {organelle}')
print(f'Taxonomy: {taxonomy}')
