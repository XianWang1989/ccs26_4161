
from Bio import Entrez
from Bio import SeqIO

# Function to fetch minimal GenBank data based on accession number
def fetch_minimal_genbank_data(accession):
    Entrez.email = "your_email@example.com"  # Always provide your email
    # Fetch the GenBank data
    handle = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text')

    # Read the record from the handle and extract only needed information
    record = SeqIO.read(handle, 'genbank')
    handle.close()

    # Extract taxonomy
    taxonomy = record.annotations.get('taxonomy', [])
    organelle = None

    # Check features for organelle information
    for feature in record.features:
        if 'organelle' in feature.qualifiers:
            organelle = feature.qualifiers['organelle'][0]
            break

    return taxonomy, organelle

# Example usage
accession1 = 'YOUR_ACCESSION_NUMBER'  # Replace with your accession number
taxonomy, organelle = fetch_minimal_genbank_data(accession1)

# Output the results
print("Taxonomy:", taxonomy)
print("Organelle:", organelle)
