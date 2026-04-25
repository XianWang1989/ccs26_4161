
from Bio import Entrez
from Bio import SeqIO

# Function to fetch and extract taxonomy and organelle from a GenBank accession number
def fetch_taxonomy_and_organelle(accession):
    Entrez.email = "your_email@example.com"  # Always provide your email
    try:
        # Fetch the GenBank record
        gb_data = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text')
        record = SeqIO.read(gb_data, 'genbank')

        # Extract taxonomy
        taxonomy = record.annotations.get('taxonomy', [])

        # Extract organelle information from features
        organelle = None
        for feature in record.features:
            if 'organelle' in feature.qualifiers:
                organelle = feature.qualifiers['organelle']
                break

        return taxonomy, organelle

    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None

# Example usage
accession_number = "NC_000852"  # Replace with your actual accession number
taxonomy, organelle = fetch_taxonomy_and_organelle(accession_number)

print("Taxonomy:", taxonomy)
print("Organelle:", organelle)
