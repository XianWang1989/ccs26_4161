
from Bio import Entrez

# Ensure you have set your email
Entrez.email = "your_email@example.com"

def fetch_taxonomy_and_organelle(accession):
    # Fetch the GenBank record
    gb_handle = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text')

    # Read the GenBank record
    gb_record = SeqIO.read(gb_handle, 'genbank')

    # Extract taxonomy
    taxonomy = gb_record.annotations.get('taxonomy', [])

    # Extract organelle from features
    organelle = None
    for feature in gb_record.features:
        if 'organelle' in feature.qualifiers:
            organelle = feature.qualifiers['organelle'][0]
            break

    return taxonomy, organelle

# Example usage
accession = 'YOUR_ACCESSION_NUMBER'
taxonomy, organelle = fetch_taxonomy_and_organelle(accession)

print("Taxonomy:", taxonomy)
print("Organelle:", organelle)
