
from Bio import SeqIO
from Bio import Entrez

# Assuming you have a list of accession numbers
accession_list = ['YOUR_ACCESSION_NUMBER']
cache = {}

for access in accession_list:
    # Fetch the GenBank file
    gb_handle = Entrez.efetch(db='nucleotide', id=access, rettype='gb', retmode='text')
    rec = SeqIO.read(gb_handle, 'genbank')
    cache[access] = rec

    # Extract organelle information
    organelle = None
    for feature in rec.features:
        if feature.type == 'source':
            if 'organelle' in feature.qualifiers:
                organelle = feature.qualifiers['organelle'][0]
            break  # We only need to check the source feature

    # Extract taxonomy information
    taxonomy = rec.annotations.get('taxonomy', [])

    # Checking conditions
    if organelle:
        print(f'Organelle for {access}: {organelle}')
    if 'Fungi' in taxonomy:
        print(f'{access} is a Fungi.')

gb_handle.close()
