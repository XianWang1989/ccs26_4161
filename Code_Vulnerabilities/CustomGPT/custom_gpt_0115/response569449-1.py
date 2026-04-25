
from Bio import Entrez
from Bio import SeqIO

# Set your email for NCBI Entrez
Entrez.email = "your_email@example.com"

# Function to fetch only the needed data
def fetch_relevant_data(accession):
    # Fetch the GenBank record
    gb_acc = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text')

    # Parse the record
    record = SeqIO.read(gb_acc, 'genbank')

    # Extract features
    organelle = None
    if record.features:
        for feat in record.features:
            if 'organelle' in feat.qualifiers:
                organelle = feat.qualifiers['organelle'][0]
                break

    # Extract taxonomy
    taxonomy = record.annotations.get('taxonomy', [])

    return organelle, taxonomy

# Example usage
accession = 'YOUR_ACCESSION_NUMBER'
organelle, taxonomy = fetch_relevant_data(accession)

# Check results
if organelle:
    print(f"Organelle: {organelle}")
if taxonomy:
    print(f"Taxonomy: {taxonomy}")
