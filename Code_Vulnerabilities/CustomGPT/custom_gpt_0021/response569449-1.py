
from Bio import Entrez
from Bio import SeqIO

def fetch_taxonomy_and_organelle(accession):
    Entrez.email = "your_email@example.com"  # Always provide your email
    # Fetch summary information
    handle = Entrez.esummary(db='nucleotide', id=accession, retmode='xml')
    record = Entrez.read(handle)
    handle.close()

    # Extract taxonomy
    taxonomy = record[0]['Taxonomy']

    # Fetch the complete record to get organelle details
    gb_handle = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text')
    gb_record = SeqIO.read(gb_handle, 'genbank')
    gb_handle.close()

    organelle = None
    for feature in gb_record.features:
        if 'organelle' in feature.qualifiers:
            organelle = feature.qualifiers['organelle'][0]

    return taxonomy, organelle

# Usage
accession_number = "YOUR_ACCESSION_NUMBER_HERE"
taxonomy, organelle = fetch_taxonomy_and_organelle(accession_number)
print(f"Taxonomy: {taxonomy}")
print(f"Organelle: {organelle}")
