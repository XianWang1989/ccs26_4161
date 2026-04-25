
from Bio import SeqIO
from Bio import Entrez

# Function to get organelle and taxonomy details
def fetch_taxonomy_and_organelle(accession):
    # Fetch the GenBank record
    with Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text') as gb_file:
        record = SeqIO.read(gb_file, 'genbank')

        # Extract taxonomy
        taxonomy = record.annotations.get('taxonomy', [])

        # Extract organelle from features
        organelle = None
        for feature in record.features:
            if 'organelle' in feature.qualifiers:
                organelle = feature.qualifiers['organelle'][0]  # Take the first organelle if multiple

        return taxonomy, organelle

# Example usage
accession_number = 'YOUR_ACCESSION_NUMBER'  # Replace with your accession number
taxonomy_info, organelle_info = fetch_taxonomy_and_organelle(accession_number)

if taxonomy_info:
    print(f"Taxonomy: {taxonomy_info}")
if organelle_info:
    print(f"Organelle: {organelle_info}")
