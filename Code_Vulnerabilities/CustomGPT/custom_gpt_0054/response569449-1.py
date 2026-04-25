
from Bio import Entrez

# Set your email (required for NCBI Entrez)
Entrez.email = "your_email@example.com"

def fetch_taxonomy_and_organelle(accession):
    # Fetch the GenBank record in XML format, which is more compact
    handle = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='xml')
    records = Entrez.read(handle)
    handle.close()

    # Extract the relevant information
    for record in records:
        # Getting taxonomy
        taxonomy = record.get('taxonomy', [])
        organelle = None

        # Extracting the specific organelle feature from the record features
        for feature in record.get('features', []):
            if feature['key'] == 'source':
                qualifiers = feature.get('qualifiers', {})
                organelle = qualifiers.get('organelle', [None])[0]  # Get the organelle value if present

        return taxonomy, organelle

# Example usage
accession_number = 'NM_001301717'  # Replace with your accession number
taxonomy, organelle = fetch_taxonomy_and_organelle(accession_number)

print("Taxonomy:", taxonomy)
print("Organelle:", organelle)
