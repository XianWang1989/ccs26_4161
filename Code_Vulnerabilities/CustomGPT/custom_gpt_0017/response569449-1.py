
from Bio import SeqIO
from Bio import Entrez

# Set your email for Entrez
Entrez.email = "your_email@example.com"

def fetch_genbank_info(accession):
    # Fetch the record
    handle = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text')
    record = SeqIO.read(handle, 'genbank')
    handle.close()

    # Extract taxonomy and organelle info
    taxonomy = record.annotations.get('taxonomy', [])
    organelle = None

    # Check for organelle feature
    for feature in record.features:
        if 'organelle' in feature.qualifiers:
            organelle = feature.qualifiers['organelle'][0]
            break

    return taxonomy, organelle

# Example usage
accession = "YOUR_ACCESSION_NUMBER"
taxonomy, organelle = fetch_genbank_info(accession)

print("Taxonomy:", taxonomy)
print("Organelle:", organelle)
