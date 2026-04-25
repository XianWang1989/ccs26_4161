
from Bio import SeqIO
from Bio import Entrez

Entrez.email = "your.email@example.com"  # Always provide your email
access1 = "YOUR_ACCESSION_NUMBER"  # Replace with your accession number

def get_organism_data(accession_num):
    # Fetch the GenBank record
    with Entrez.efetch(db='nucleotide', id=accession_num, rettype='gb', retmode='text') as gb_data:
        rec = SeqIO.read(gb_data, 'genbank')

    # Extract organelle and taxonomy from the fetched record
    organelle = None
    taxonomy = rec.annotations.get('taxonomy', [])

    for feature in rec.features:
        if 'organelle' in feature.qualifiers:
            organelle = feature.qualifiers['organelle'][0]

    return organelle, taxonomy

# Example usage
organelle, taxonomy = get_organism_data(access1)
print(f'Organelle: {organelle}, Taxonomy: {taxonomy}')
