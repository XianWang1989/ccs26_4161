
from Bio import SeqIO
from Bio import Entrez

# Ensure that your email is set up for NCBI Entrez
Entrez.email = "your_email@example.com"

# Function to retrieve only necessary features
def fetch_genbank_data(accession):
    # Fetch the GenBank record
    with Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text') as gb_file:
        # Read the record while it's still open
        record = SeqIO.read(gb_file, 'genbank')

        # Extract only the relevant features
        organelle_info = None
        taxonomy_info = record.annotations.get('taxonomy', [])

        # Check for organelle info in features
        for feature in record.features:
            if 'organelle' in feature.qualifiers:
                organelle_info = feature.qualifiers['organelle'][0]
                break

        return organelle_info, taxonomy_info

# Example usage
accession_number = "ACCESSION_NUMBER_HERE"
organelle, taxonomy = fetch_genbank_data(accession_number)

print(f"Organelle: {organelle}")
print(f"Taxonomy: {taxonomy}")
