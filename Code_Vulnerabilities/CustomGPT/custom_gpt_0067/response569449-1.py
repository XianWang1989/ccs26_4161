
from Bio import SeqIO
from Bio import Entrez

# Initialize Entrez email
Entrez.email = 'your_email@example.com'

def fetch_partial_genbank(accession):
    # Fetch GenBank record
    gb_handle = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text')

    # Read the GenBank record
    record = SeqIO.read(gb_handle, 'genbank')

    # Extract taxonomy if available
    taxonomy = record.annotations.get('taxonomy', [])

    # Extract organelle from features if available
    organelle = None
    for feat in record.features:
        if 'organelle' in feat.qualifiers:
            organelle = feat.qualifiers['organelle'][0]
            break

    return taxonomy, organelle

# Example usage
accession = "YOUR_ACCESSION_NUMBER"
taxonomy, organelle = fetch_partial_genbank(accession)

if taxonomy and taxonomy[1] == 'Fungi':
    print("This record is from Fungi.")
if organelle:
    print(f"Organelle: {organelle}")
