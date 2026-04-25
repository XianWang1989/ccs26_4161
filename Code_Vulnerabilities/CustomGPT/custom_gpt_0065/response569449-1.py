
from Bio import Entrez
from Bio import SeqIO

# Function to fetch taxonomy and organelle information
def fetch_taxonomy_organelle(accession):
    Entrez.email = "your_email@example.com"  # Always provide your email
    # Fetch the record with minimal data
    handle = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text', 
                           seq_start=None, seq_stop=None)

    # Parse the GenBank record
    record = SeqIO.read(handle, 'genbank')
    handle.close()

    # Extract taxonomy
    taxonomy = record.annotations.get('taxonomy', [])
    organelle = None
    # Iterate through features to find organelle information
    for feature in record.features:
        if 'organelle' in feature.qualifiers:
            organelle = feature.qualifiers['organelle'][0]

    return taxonomy, organelle

# Example usage
accession = "YOUR_ACCESSION_NUMBER"
taxonomy, organelle = fetch_taxonomy_organelle(accession)
print("Taxonomy:", taxonomy)
print("Organelle:", organelle)
