
from Bio import Entrez
from Bio import SeqIO

Entrez.email = "your_email@example.com"  # Always set your email

def fetch_taxonomy_and_organelle(accession):
    # Fetch the record in XML format
    handle = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='xml')
    records = SeqIO.parse(handle, 'GenBank')
    for record in records:
        # Extract taxonomy
        taxonomy = record.annotations.get('taxonomy', [])
        organelle = None
        for feature in record.features:
            if feature.type == 'source':
                organelle = feature.qualifiers.get('organelle', None)
                break

        # Process the information
        if taxonomy and 'Fungi' in taxonomy:
            print(f"{accession}: Found in taxonomy - Fungi")
        if organelle:
            print(f"{accession}: Organelle - {organelle[0]}")

# Example usage
accession_numbers = ["ABC123", "DEF456"]
for acc in accession_numbers:
    fetch_taxonomy_and_organelle(acc)
