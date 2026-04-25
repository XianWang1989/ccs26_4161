
from Bio import Entrez
from Bio import SeqIO

# Function to fetch taxonomy and organelle information
def fetch_taxonomy_and_organelle(accession):
    # Fetching the GenBank file
    handle = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text')

    # Parsing the GenBank record
    record = SeqIO.read(handle, 'genbank')
    handle.close()

    # Extracting taxonomy and organelle information
    taxonomy = record.annotations.get('taxonomy', [])
    organelle = None
    for feature in record.features:
        if 'organelle' in feature.qualifiers:
            organelle = feature.qualifiers['organelle'][0]  # Get the first organelle description
            break

    return taxonomy, organelle

# Example usage
Entrez.email = "your_email@example.com"  # Always provide your email
accession = "ABC123"  # Replace with your accession number
taxonomy_info, organelle_info = fetch_taxonomy_and_organelle(accession)

print("Taxonomy:", taxonomy_info)
print("Organelle:", organelle_info)
