
from Bio import SeqIO
from Bio import Entrez

# Make sure to set up your email
Entrez.email = "your_email@example.com"

def fetch_taxonomy_and_organelle(accession):
    gb_data = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text', 
                            seq_start=0, seq_stop=1)  # Limits sequence data

    # Read the GenBank record
    record = SeqIO.read(gb_data, 'genbank')

    # Extract the organelle information if available
    organelle = None
    for feature in record.features:
        if feature.type == 'source':
            organelle = feature.qualifiers.get('organelle', [None])[0]

    # Extract the taxonomy information
    taxonomy = record.annotations.get('taxonomy', [])

    return organelle, taxonomy

# Example usage
accession = "YOUR_ACCESSION_NUMBER"
organelle, taxonomy = fetch_taxonomy_and_organelle(accession)

if organelle:
    print(f"Organelle: {organelle}")
if taxonomy:
    print(f"Taxonomy: {taxonomy}")
