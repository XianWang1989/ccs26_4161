
from Bio import Entrez
from Bio import SeqIO

# Function to fetch only the taxonomy information
def fetch_taxonomy_info(accession):
    Entrez.email = "your_email@example.com"  # Always set your email for NCBI
    handle = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text')

    # Read the GenBank file
    record = SeqIO.read(handle, 'genbank')
    handle.close()

    # Return taxonomy information if available
    return record.annotations.get('taxonomy', [])

# Function to fetch organelle info
def fetch_organelle_info(accession):
    Entrez.email = "your_email@example.com"  # Always set your email for NCBI
    handle = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text')

    # Read the GenBank file
    record = SeqIO.read(handle, 'genbank')
    handle.close()

    # Extract organelle information
    organelle_info = []
    for feature in record.features:
        if 'organelle' in feature.qualifiers:
            organelle_info.extend(feature.qualifiers['organelle'])
    return organelle_info

accessions = [access1, access2, access3]  # Replace with your list of accession numbers
fungi_count = 0

for accession in accessions:
    # Fetch taxonomy info
    taxonomy = fetch_taxonomy_info(accession)
    if taxonomy and taxonomy[1] == 'Fungi':
        fungi_count += 1

    # Fetch organelle info
    organelle = fetch_organelle_info(accession)
    print(f'Accession: {accession}, Taxonomy: {taxonomy}, Organelle: {organelle}')

print(f'Total Fungi Count: {fungi_count}')
