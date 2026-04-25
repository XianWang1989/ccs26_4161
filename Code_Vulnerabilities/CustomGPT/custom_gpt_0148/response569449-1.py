
from Bio import Entrez
from Bio import SeqIO

# Set email for Entrez
Entrez.email = "your_email@example.com"

def fetch_taxonomy_and_organelle(accession):
    # Fetch only the metadata for the given accession number
    handle = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text')

    # Read the GenBank record
    record = SeqIO.read(handle, 'genbank')
    handle.close()

    # Get taxonomy and organelle
    taxonomy = record.annotations.get('taxonomy', [])
    organelle = ""

    for feature in record.features:
        if 'organelle' in feature.qualifiers:
            organelle = feature.qualifiers['organelle'][0]
            break

    return taxonomy, organelle

# Example usage
accession_number = "AB123456"  # Replace with actual accession number
taxonomy, organelle = fetch_taxonomy_and_organelle(accession_number)

print("Taxonomy:", taxonomy)
print("Organelle:", organelle)
