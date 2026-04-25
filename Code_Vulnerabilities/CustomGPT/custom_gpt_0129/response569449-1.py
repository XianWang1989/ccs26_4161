
from Bio import SeqIO
from Bio import Entrez

# Function to fetch and parse only taxonomy and organelle information
def fetch_taxonomy_and_organelle(accession):
    # Fetch the GenBank file
    gb_file = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text')

    # Read the record
    record = SeqIO.read(gb_file, 'genbank')

    # Extracting taxonomy information
    taxonomy = record.annotations.get('taxonomy', [])

    # Extracting organelle information if available
    organelle = None
    for feature in record.features:
        if 'organelle' in feature.qualifiers:
            organelle = feature.qualifiers['organelle'][0]  # Get the first organelle if multiple

    return taxonomy, organelle

# Example usage
accession_number = 'YOUR_ACCESSION_NUMBER_HERE'
taxonomy, organelle = fetch_taxonomy_and_organelle(accession_number)

print("Taxonomy:", taxonomy)
print("Organelle:", organelle)
