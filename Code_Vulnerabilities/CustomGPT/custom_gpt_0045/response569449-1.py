
from Bio import Entrez
from Bio import SeqIO

# Set your email for Entrez
Entrez.email = "your.email@example.com"

def fetch_taxonomy_and_organelle(accession):
    # Fetch the summary of the GenBank record
    summary_handle = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text')

    # Read the summary
    record = SeqIO.read(summary_handle, 'genbank')

    # Get taxonomy information
    taxonomy = record.annotations.get('taxonomy', [])

    # Initialize an organelle variable
    organelle = None

    # Check features for organelle annotation
    for feature in record.features:
        if 'organelle' in feature.qualifiers:
            organelle = feature.qualifiers['organelle'][0]
            break

    return taxonomy, organelle

# Example usage
accessions = ["YOUR_ACCESSION_NUMBER"]  # Replace with your accession numbers
for acc in accessions:
    taxonomy, organelle = fetch_taxonomy_and_organelle(acc)
    print(f"Accession: {acc}, Taxonomy: {taxonomy}, Organelle: {organelle}")
