
from Bio import Entrez
from Bio import SeqIO

Entrez.email = "your_email@example.com"  # Always include your email

def fetch_taxonomy_and_organelle(accession):
    # Fetch only the header information and features
    handle = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text')
    record = SeqIO.read(handle, 'genbank')

    # Extracting taxonomy
    taxonomy = record.annotations.get('taxonomy', [])

    # Extracting organelle feature if present
    organelle = None
    for feature in record.features:
        if 'organelle' in feature.qualifiers:
            organelle = feature.qualifiers['organelle'][0]
            break

    return taxonomy, organelle

# Example usage
accession_number = 'YOUR_ACCESSION_NUMBER'  # Replace with actual accession
taxonomy, organelle = fetch_taxonomy_and_organelle(accession_number)

print("Taxonomy:", taxonomy)
print("Organelle:", organelle)
