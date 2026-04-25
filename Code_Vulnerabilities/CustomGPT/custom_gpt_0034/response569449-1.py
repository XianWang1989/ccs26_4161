
from Bio import SeqIO
from Bio import Entrez

# Set your email for Entrez
Entrez.email = "your_email@example.com"

def fetch_organism_info(accession):
    # Fetch the GenBank record
    with Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text') as gb_file:
        record = SeqIO.read(gb_file, 'genbank')

        # Extract taxonomy information
        taxonomy = record.annotations.get('taxonomy', [])

        # Initialize organelle variable
        organelle_info = None
        for feature in record.features:
            if 'organelle' in feature.qualifiers:
                organelle_info = feature.qualifiers['organelle'][0]
                break

        return taxonomy, organelle_info

# Example usage
accession_number = "NM_001301717"  # Replace with actual access number
taxonomy, organelle = fetch_organism_info(accession_number)

if taxonomy:
    print("Taxonomy:", taxonomy)
if organelle:
    print("Organelle:", organelle)
