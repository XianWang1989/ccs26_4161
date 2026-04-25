
from Bio import Entrez
from Bio import SeqIO

# Ensure you have provided the email as required by NCBI Entrez
Entrez.email = "your_email@example.com"

def fetch_taxonomy_and_organelle(accession):
    # Fetch only the records to minimize the data volume
    handle = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text')

    # Read the GenBank record
    record = SeqIO.read(handle, 'genbank')
    handle.close()

    # Initialize variables for taxonomy and organelle
    taxonomy = None
    organelle = None

    # Extract taxonomy from annotations if available
    if 'taxonomy' in record.annotations:
        taxonomy = record.annotations['taxonomy']

    # Extract organelle from features if available
    for feature in record.features:
        if 'organelle' in feature.qualifiers:
            organelle = feature.qualifiers['organelle']
            break  # Exit after finding the first organelle

    return taxonomy, organelle

accession_number = "YOUR_ACCESSION_NUMBER"
taxonomy, organelle = fetch_taxonomy_and_organelle(accession_number)

# Sample output
if taxonomy:
    print("Taxonomy:", taxonomy)
else:
    print("No taxonomy information found.")

if organelle:
    print("Organelle:", organelle)
else:
    print("No organelle information found.")
