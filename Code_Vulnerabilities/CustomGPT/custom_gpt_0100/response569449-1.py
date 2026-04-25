
from Bio import SeqIO
from Bio import Entrez

Entrez.email = "your_email@example.com"  # Always include your email!

def fetch_taxonomy_and_organelle(accession):
    # Fetch the GenBank file
    handle = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text')
    record = SeqIO.read(handle, 'genbank')
    handle.close()  # Close the handle after reading

    # Extract taxonomy
    taxonomy = record.annotations.get('taxonomy', [])
    # Extract organelle information
    organelle = None
    for feature in record.features:
        if 'organelle' in feature.qualifiers:
            organelle = feature.qualifiers['organelle'][0]
            break

    return taxonomy, organelle

# Example usage
accession_list = ['ACCESSION_1', 'ACCESSION_2']  # Replace with actual accession numbers
for accession in accession_list:
    taxonomy, organelle = fetch_taxonomy_and_organelle(accession)
    print(f'Accession: {accession}, Taxonomy: {taxonomy}, Organelle: {organelle}')
