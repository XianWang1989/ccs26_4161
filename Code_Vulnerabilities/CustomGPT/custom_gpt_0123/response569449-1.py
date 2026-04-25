
from Bio import SeqIO
from Bio import Entrez

# Set your email for Entrez
Entrez.email = "your_email@example.com"

def fetch_taxonomy_and_organelle(access1):
    gb_acc = Entrez.efetch(db='nucleotide', id=access1, rettype='gb', retmode='text')
    rec = SeqIO.read(gb_acc, 'genbank')

    # Check for taxonomy
    taxonomy = rec.annotations.get('taxonomy', [])
    if 'Fungi' in taxonomy:
        fungi_count = 1  # Increment your fungi counter

    # Extract organelle feature if available
    organelle_info = None
    for feature in rec.features:
        if 'organelle' in feature.qualifiers:
            organelle_info = feature.qualifiers['organelle']
            break

    return taxonomy, organelle_info, fungi_count

# Example usage
accession_numbers = ['YOUR_ACCESSION_NUMBER_HERE']
for access1 in accession_numbers:
    taxonomy, organelle, fungi = fetch_taxonomy_and_organelle(access1)
    print(f'Taxonomy: {taxonomy}, Organelle: {organelle}, Fungi Count: {fungi}')
