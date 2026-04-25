
from Bio import Entrez
from Bio import SeqIO

# Initialize Entrez
Entrez.email = "your_email@example.com"  # Always provide your email

def fetch_taxonomy_and_organelle(accession):
    # Fetch the record
    gb_record = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text')

    # Parsing the GenBank record
    record = SeqIO.read(gb_record, 'genbank')

    # Extracting taxonomy
    taxonomy = record.annotations.get('taxonomy', [])
    organelle = None
    for feature in record.features:
        if 'organelle' in feature.qualifiers:
            organelle = feature.qualifiers['organelle'][0]  # Get the first organelle

    return taxonomy, organelle

# Example usage
accession_number = "YOUR_ACCESSION_NUMBER"  # Replace with your actual accession number
taxonomy, organelle = fetch_taxonomy_and_organelle(accession_number)

# Output results
print(f"Taxonomy: {taxonomy}")
print(f"Organelle: {organelle}")
