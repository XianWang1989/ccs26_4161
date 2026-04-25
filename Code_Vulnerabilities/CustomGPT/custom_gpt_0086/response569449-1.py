
from Bio import Entrez, SeqIO

# Define your Entrez email
Entrez.email = "your_email@example.com"

# Function to get taxonomy and organelle information
def fetch_taxonomy_and_organelle(accession):
    # Fetch the summary of the record
    handle = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text')

    # Parse the record
    record = SeqIO.read(handle, 'genbank')
    handle.close()

    # Get taxonomy
    taxonomy = record.annotations.get('taxonomy', [])

    # Get organelle information from features
    organelle = None
    for feature in record.features:
        if 'organelle' in feature.qualifiers:
            organelle = feature.qualifiers['organelle'][0]
            break

    return taxonomy, organelle

# Example usage
accession = 'YOUR_ACCESSION_NUMBER'
taxonomy, organelle = fetch_taxonomy_and_organelle(accession)

print("Taxonomy:", taxonomy)
print("Organelle:", organelle)
