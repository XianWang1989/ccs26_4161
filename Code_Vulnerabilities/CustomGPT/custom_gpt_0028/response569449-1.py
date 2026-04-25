
from Bio import SeqIO
from Bio import Entrez

# Set your email for Entrez
Entrez.email = "your_email@example.com"

def fetch_taxonomy_and_organelle(accession):
    # Fetch the GenBank record
    handle = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text')
    record = SeqIO.read(handle, 'genbank')
    handle.close()

    # Extract taxonomy
    taxonomy = record.annotations.get('taxonomy', [])
    organelle = None

    # Extract organelle feature if present
    for feature in record.features:
        if feature.type == 'source' and 'organelle' in feature.qualifiers:
            organelle = feature.qualifiers['organelle'][0]  # Get the first organelle entry

    return taxonomy, organelle

# Example usage
accession_number = 'YOUR_ACCESSION_NUMBER'
taxonomy, organelle = fetch_taxonomy_and_organelle(accession_number)

print('Taxonomy:', taxonomy)
print('Organelle:', organelle)
