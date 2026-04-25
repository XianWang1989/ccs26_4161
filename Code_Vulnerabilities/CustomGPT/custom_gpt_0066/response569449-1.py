
from Bio import Entrez
from Bio import SeqIO

def fetch_genbank_info(accession):
    # Use Entrez to fetch only the metadata
    handle = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text')
    record = SeqIO.read(handle, 'genbank')

    # Extract the taxonomy
    taxonomy = record.annotations.get('taxonomy', [])

    # Extract organelle from features
    organelle = None
    for feature in record.features:
        if 'organelle' in feature.qualifiers:
            organelle = feature.qualifiers['organelle'][0]  # Get the first organelle if multiple

    return taxonomy, organelle

# Example usage
accession_list = ['ACCESSION1', 'ACCESSION2']  # Replace with your actual accession numbers
for accession in accession_list:
    taxonomy, organelle = fetch_genbank_info(accession)
    print(f'Accession: {accession}, Taxonomy: {taxonomy}, Organelle: {organelle}')
