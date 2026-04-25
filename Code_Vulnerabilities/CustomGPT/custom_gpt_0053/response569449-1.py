
from Bio import Entrez
from Bio import SeqIO

# Function to fetch and extract only taxonomy and organelle
def fetch_taxonomy_and_organelle(accession):
    Entrez.email = "your_email@example.com"  # Always set your email
    # Fetching the GenBank record
    with Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text') as gb_handle:
        for record in SeqIO.parse(gb_handle, 'genbank'):
            # Extracting taxonomy
            taxonomy = record.annotations.get('taxonomy', [])
            # Extracting organelle information
            organelle = None
            for feature in record.features:
                if 'organelle' in feature.qualifiers:
                    organelle = feature.qualifiers['organelle'][0]
                    break

            return taxonomy, organelle

# Example usage
accession_number = "YOUR_ACCESSION_NUMBER_HERE"
taxonomy, organelle = fetch_taxonomy_and_organelle(accession_number)

print("Taxonomy:", taxonomy)
print("Organelle:", organelle)
