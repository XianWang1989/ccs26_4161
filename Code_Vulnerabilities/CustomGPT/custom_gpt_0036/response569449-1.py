
from Bio import SeqIO
from Bio import Entrez

# Set up Entrez email
Entrez.email = "your_email@example.com"

# Function to fetch and process specific features from GenBank
def get_taxonomy_and_organelle(accession):
    # Fetch the GenBank record
    with Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text') as gb_file:
        # Read the record directly
        record = SeqIO.read(gb_file, 'genbank')

        # Extract taxonomy
        taxonomy = record.annotations.get('taxonomy', [])
        # Check if taxonomy information is available
        if len(taxonomy) > 1 and taxonomy[1] == 'Fungi':
            print(f"{accession} belongs to Fungi")

        # Extract organelle feature if available
        for feature in record.features:
            if feature.type == 'gene' and 'organelle' in feature.qualifiers:
                organelle = feature.qualifiers['organelle']
                print(f"{accession} organelle: {organelle}")

# Example usage
accession_number = 'YOUR_ACCESSION_NUMBER'
get_taxonomy_and_organelle(accession_number)
