
from Bio import SeqIO
from Bio import Entrez

# Function to fetch organelle and taxonomy information directly
def fetch_taxonomy_and_organelle(access):
    # Fetch the GenBank record
    with Entrez.efetch(db='nucleotide', id=access, rettype='gb', retmode='text') as gb_file:
        for record in SeqIO.parse(gb_file, 'genbank'):
            # Extract taxonomy
            taxonomy = record.annotations.get('taxonomy', [])
            organelle = None

            # Check for features to find organelle
            for feature in record.features:
                if 'organelle' in feature.qualifiers:
                    organelle = feature.qualifiers['organelle']
                    break

            return taxonomy, organelle

# Usage example
accession = "YOUR_ACCESSION_NUMBER"  # Replace with your accession number
taxonomy, organelle = fetch_taxonomy_and_organelle(accession)

print(f"Taxonomy: {taxonomy}")
if organelle:
    print(f"Organelle: {organelle[0]}")  # Accessing the first organelle feature if available
else:
    print("Organelle feature not found.")
