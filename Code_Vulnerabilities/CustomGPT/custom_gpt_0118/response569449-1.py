
from Bio import SeqIO
from Bio import Entrez

def fetch_genbank_info(accession):
    # Fetch the whole GenBank file
    with Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text') as gb_file:
        record = SeqIO.read(gb_file, 'genbank')

    # Extract organelle information
    organelle = None
    for feature in record.features:
        if 'organelle' in feature.qualifiers:
            organelle = feature.qualifiers['organelle'][0]
            break  # Stop after finding the first organelle

    # Extract taxonomy information
    taxonomy = record.annotations.get('taxonomy', [])

    return organelle, taxonomy

# Usage
accession_numbers = ['ACCESSION_1', 'ACCESSION_2']  # Replace with actual accession numbers
results = {}

for accession in accession_numbers:
    organelle, taxonomy = fetch_genbank_info(accession)
    results[accession] = {'organelle': organelle, 'taxonomy': taxonomy}

print(results)
