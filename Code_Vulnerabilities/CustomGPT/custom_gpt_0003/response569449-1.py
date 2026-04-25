
from Bio import Entrez
from Bio import SeqIO

# Set up Entrez email
Entrez.email = "your_email@example.com"

def fetch_taxonomy(access):
    """Fetch taxonomy for a given accession number."""
    handle = Entrez.esummary(db='nucleotide', id=access)
    records = Entrez.read(handle)
    handle.close()

    # Get taxonomy information
    taxonomy = records[0]['Taxonomy']
    return taxonomy

def fetch_organelle(access):
    """Fetch the organelle from the GenBank record."""
    gb_acc = Entrez.efetch(db='nucleotide', id=access, rettype='gb', retmode='text')
    rec = SeqIO.read(gb_acc, 'genbank')

    # Extract organelle information, if available
    organelle = None
    for feature in rec.features:
        if 'organelle' in feature.qualifiers:
            organelle = feature.qualifiers['organelle'][0]
            break

    return organelle

# Example usage
access1 = "YOUR_ACCESSION_NUMBER"
taxonomy = fetch_taxonomy(access1)

if taxonomy and taxonomy[1] == 'Fungi':
    print(f"Taxonomy indicates Fungi for {access1}")

organelle = fetch_organelle(access1)
if organelle:
    print(f"Organelle found: {organelle}")
