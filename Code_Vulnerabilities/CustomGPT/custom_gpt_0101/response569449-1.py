
from Bio import Entrez
from Bio import SeqIO

def fetch_taxonomy_and_organelle(accession):
    Entrez.email = "your_email@example.com"  # Replace with your email
    handle = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text')
    record = SeqIO.read(handle, 'genbank')
    handle.close()

    taxonomy = record.annotations.get('taxonomy', [])
    organelle = next((feat.qualifiers['organelle'][0] for feat in record.features if 'organelle' in feat.qualifiers), None)

    return taxonomy, organelle

# Example usage
accession_number = "YOUR_ACCESSION_NUMBER"  # Replace with the actual accession number
taxonomy, organelle = fetch_taxonomy_and_organelle(accession_number)

print(f"Taxonomy: {taxonomy}")
print(f"Organelle: {organelle}")
