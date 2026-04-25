
from Bio import SeqIO
from Bio import Entrez

# Use your own email
Entrez.email = "your_email@example.com"

def fetch_taxonomy_and_organelle(accession):
    # Fetch the GenBank record
    with Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text') as handle:
        record = SeqIO.read(handle, 'genbank')

    # Extracting taxonomy
    taxonomy = record.annotations.get('taxonomy', [])
    organelle = None

    # Searching for organelle feature
    for feature in record.features:
        if 'organelle' in feature.qualifiers:
            organelle = feature.qualifiers['organelle'][0]
            break

    return taxonomy, organelle

# Example usage
accession_number = "YOUR_ACCESSION_NUMBER"
taxonomy, organelle = fetch_taxonomy_and_organelle(accession_number)

# Check results
print("Taxonomy:", taxonomy)
print("Organelle:", organelle)
