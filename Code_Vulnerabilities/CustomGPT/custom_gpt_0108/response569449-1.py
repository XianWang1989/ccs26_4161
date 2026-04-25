
from Bio import SeqIO
from Bio import Entrez

# Set your email for Entrez
Entrez.email = "your_email@example.com"

def fetch_genbank_data(accession):
    # Fetch the GenBank record
    gb_file = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text')
    record = SeqIO.read(gb_file, 'genbank')

    # Extract the organelle information
    organelle = None
    for feature in record.features:
        if 'organelle' in feature.qualifiers:
            organelle = feature.qualifiers['organelle'][0]

    # Extract the taxonomy
    taxonomy = record.annotations.get('taxonomy', [])

    return organelle, taxonomy

# Example usage
accession_number = "YOUR_ACCESSION_NUMBER"
organelle, taxonomy = fetch_genbank_data(accession_number)

print("Organelle:", organelle)
print("Taxonomy:", taxonomy)
