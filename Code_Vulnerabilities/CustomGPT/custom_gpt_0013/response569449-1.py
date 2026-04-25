
from Bio import Entrez
from Bio import SeqIO

Entrez.email = "your_email@example.com"  # Always include your email!

def fetch_taxonomy_and_organelle(accession):
    # Fetch the metadata only
    handle = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text')
    record = SeqIO.read(handle, 'genbank')

    # Extract taxonomy
    taxonomy = record.annotations.get('taxonomy', [])
    organelle = None

    # Look for organelle in features
    for feature in record.features:
        if 'organelle' in feature.qualifiers:
            organelle = feature.qualifiers['organelle'][0]
            break  # No need to continue if already found

    return taxonomy, organelle

# Example usage
accession = "ABC123"
taxonomy_info, organelle_info = fetch_taxonomy_and_organelle(accession)

if 'Fungi' in taxonomy_info:
    print("This accession is a Fungi.")
if organelle_info:
    print(f"Organelle info: {organelle_info}")
