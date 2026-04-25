
from Bio import SeqIO
from Bio import Entrez

# Function to fetch and parse specific features
def fetch_genbank_feature(accession):
    Entrez.email = "your_email@example.com"  # Always set your email
    # Fetch the GenBank record
    with Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text') as gb_file:
        # Read the record
        record = SeqIO.read(gb_file, 'genbank')

        # Extract organelle
        organelle = None
        for feature in record.features:
            if feature.type == 'source' and 'organelle' in feature.qualifiers:
                organelle = feature.qualifiers['organelle'][0]
                break

        # Extract taxonomy
        taxonomy = record.annotations.get('taxonomy', [])

        return organelle, taxonomy

# Example usage
accession_numbers = ['access1', 'access2', 'access3']  # Replace with your accession numbers
for acc in accession_numbers:
    organelle, taxonomy = fetch_genbank_feature(acc)
    if organelle:
        print(f"Accession: {acc}, Organelle: {organelle}")
    if 'Fungi' in taxonomy:
        print(f"Accession: {acc} belongs to Fungi.")
