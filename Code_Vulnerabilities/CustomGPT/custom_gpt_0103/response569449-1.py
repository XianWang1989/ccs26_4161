
from Bio import SeqIO
from Bio import Entrez

Entrez.email = "your_email@example.com"  # Replace with your email

def fetch_taxonomy_and_organelle(accession):
    # Fetch GenBank record
    handle = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text')
    record = SeqIO.read(handle, 'genbank')

    # Extract taxonomy
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

print(f"Taxonomy: {taxonomy}")
print(f"Organelle: {organelle}")
