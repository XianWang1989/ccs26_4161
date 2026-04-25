
from Bio import SeqIO
from Bio import Entrez

# Set your email
Entrez.email = "your_email@example.com"

def fetch_taxonomy_and_organelle(accession):
    # Fetch the GenBank record
    handle = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text')
    record = SeqIO.read(handle, 'genbank')
    handle.close()

    # Extract the taxonomy
    taxonomy = record.annotations.get('taxonomy', [])
    organelle = None

    # Find the organelle feature
    for feature in record.features:
        if feature.type == 'organelle':
            organelle = feature.qualifiers.get('organelle', ['N/A'])[0]  # Default to 'N/A' if not found

    return taxonomy, organelle

# Example usage
accession_number = "YOUR_ACCESSION_NUMBER"
taxonomy, organelle = fetch_taxonomy_and_organelle(accession_number)
print(f'Taxonomy: {taxonomy}')
print(f'Orgelale: {organelle}')
