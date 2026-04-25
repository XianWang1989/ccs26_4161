
from Bio import Entrez
from Bio import SeqIO

# Function to fetch specific information from a GenBank file
def fetch_genbank_info(accession):
    Entrez.email = "your_email@example.com"  # Always set your email
    handle = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text')

    # Read the GenBank record
    for record in SeqIO.parse(handle, 'genbank'):
        # Extract taxonomy
        taxonomy = record.annotations.get('taxonomy', [])
        # Initialize organelle variable
        organelles = []

        # Gather organelle information
        for feature in record.features:
            if 'organelle' in feature.qualifiers:
                organelles.extend(feature.qualifiers['organelle'])

        return taxonomy, organelles

# Usage
accession_number = 'YOUR_ACCESSION_NUMBER'  # Replace with actual accession number
taxonomy_info, organelle_info = fetch_genbank_info(accession_number)

print("Taxonomy:", taxonomy_info)
print("Organelle:", organelle_info)
