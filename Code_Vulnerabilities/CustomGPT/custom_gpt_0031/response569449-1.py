
from Bio import Entrez
from Bio import SeqIO

# Ensure to always provide your email to Entrez
Entrez.email = "your_email@example.com"

def fetch_taxonomy_and_organelle(accession):
    handle = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text')
    record = SeqIO.read(handle, 'genbank')
    handle.close()

    # Extracting needed information
    taxonomy = record.annotations.get('taxonomy', [])
    organelle = None

    for feature in record.features:
        if 'organelle' in feature.qualifiers:
            organelle = feature.qualifiers['organelle'][0]
            break

    return taxonomy, organelle

# Example usage
accession_number = "YOUR_ACCESSION_NUMBER"
taxonomy, organelle = fetch_taxonomy_and_organelle(accession_number)

# Output the results
print("Taxonomy:", taxonomy)
print("Organelle:", organelle if organelle else "Not found")
