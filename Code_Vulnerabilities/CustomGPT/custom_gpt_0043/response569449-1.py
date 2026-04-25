
from Bio import Entrez
from Bio import SeqIO

def get_taxonomy_and_organelle(accession):
    # Fetch the GenBank record
    handle = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text')

    # Read the GenBank record from the handle
    record = SeqIO.read(handle, 'genbank')

    # Extract taxonomy if available
    taxonomy = record.annotations.get('taxonomy', None)

    # Check for organelle in features
    organelle = None
    for feature in record.features:
        if 'organelle' in feature.qualifiers:
            organelle = feature.qualifiers['organelle'][0]
            break

    # Close the handle
    handle.close()

    return taxonomy, organelle

# Example usage
accession_number = 'INSERT_ACCESSION_HERE'  # replace with your accession number
taxonomy, organelle = get_taxonomy_and_organelle(accession_number)

if taxonomy and 'Fungi' in taxonomy:
    print(f'Taxonomy: {taxonomy}, Organelle: {organelle}')
else:
    print('Not categorized as Fungi or missing information.')
