
from Bio import SeqIO
from Bio import Entrez

# This is where you set your email to use Entrez
Entrez.email = 'your_email@example.com'

def fetch_organism_info(access):
    # Fetch the GenBank record
    gb_acc = Entrez.efetch(db='nucleotide', id=access, rettype='gb', retmode='text')   
    rec = SeqIO.read(gb_acc, 'genbank')

    # Initiate a dictionary to cache results
    data = {}

    # Get taxonomy and organelle information
    if 'taxonomy' in rec.annotations:
        data['taxonomy'] = rec.annotations['taxonomy']
    else:
        data['taxonomy'] = None

    for feat in rec.features:
        if feat.type == 'source':
            # Check for organelle information
            if 'organelle' in feat.qualifiers:
                data['organelle'] = feat.qualifiers['organelle'][0]
            else:
                data['organelle'] = None

    return data

# Example usage:
accession_number = 'YOUR_ACCESSION_NUMBER'  # Replace with a valid accession number
info = fetch_organism_info(accession_number)

print(f"Taxonomy: {info['taxonomy']}")
print(f"Organelle: {info['organelle']}")
