
from Bio import SeqIO
from Bio import Entrez

# Function to get organelle and taxonomy information
def fetch_genbank_features(accession):
    Entrez.email = "your_email@example.com"  # Provide your email
    # Fetch the GenBank record
    with Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text') as gb_file:
        record = SeqIO.read(gb_file, 'genbank')

        # Extract taxonomy
        taxonomy = record.annotations.get('taxonomy', [])
        organelle = None

        # Extract organelle from features
        for feature in record.features:
            if feature.type == 'source':
                organelle = feature.qualifiers.get('organelle', [None])[0]
                break

        return taxonomy, organelle

# Example usage
accession_number = 'YOUR_ACCESSION_NUMBER'
taxonomy, organelle = fetch_genbank_features(accession_number)

if taxonomy and 'Fungi' in taxonomy:
    print("This organism belongs to Fungi.")
if organelle:
    print(f"Organelle: {organelle}")
