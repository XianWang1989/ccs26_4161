
from Bio import SeqIO
from Bio import Entrez

# Function to fetch and parse specific features from a GenBank file
def fetch_genbank_features(accession):
    Entrez.email = "your_email@example.com"  # Always include your email
    handle = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text')

    # Read the GenBank record
    record = SeqIO.read(handle, 'genbank')
    handle.close()

    # Extract organelle information
    organelle = None
    for feature in record.features:
        if feature.type == 'source':
            if 'organelle' in feature.qualifiers:
                organelle = feature.qualifiers['organelle'][0]

    # Extract taxonomy information
    taxonomy = record.annotations.get('taxonomy', [])

    return taxonomy, organelle

# Example usage
accession_number = 'YOUR_ACCESSION_NUMBER'
taxonomy, organelle = fetch_genbank_features(accession_number)

print("Taxonomy:", taxonomy)
print("Organelle:", organelle)
