
from Bio import Entrez
from Bio import SeqIO

# Set your email for Entrez
Entrez.email = "your_email@example.com"

# Function to fetch taxonomy and organelle info
def fetch_taxonomy_and_organelle(accession):
    # Use the 'gb' rettype to get the GenBank format but limit the output
    handle = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text')

    # Parse the GenBank file
    record = SeqIO.read(handle, 'genbank')

    # Initialize results
    taxonomy = None
    organelle = None

    # Extract taxonomy if available
    if 'taxonomy' in record.annotations:
        taxonomy = record.annotations['taxonomy']

    # Extract organelle feature if available
    for feature in record.features:
        if 'organelle' in feature.qualifiers:
            organelle = feature.qualifiers['organelle'][0]
            break

    return taxonomy, organelle

# Example usage
accession_number = "YOUR_ACCESSION_NUMBER"
taxonomy, organelle = fetch_taxonomy_and_organelle(accession_number)

print("Taxonomy:", taxonomy)
print("Organelle:", organelle)
