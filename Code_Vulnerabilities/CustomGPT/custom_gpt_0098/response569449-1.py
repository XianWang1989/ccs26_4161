
from Bio import Entrez

# Set your email for NCBI
Entrez.email = "your_email@example.com"

def fetch_taxonomy_and_organelle(accession):
    # Fetch just the taxonomy information
    handle = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='xml')
    records = Entrez.read(handle)
    handle.close()

    # Extract relevant information
    for record in records:
        # Check for taxonomy
        taxonomy = record['GBSeq_taxonomy']
        # Extract organelle if present
        organelle = None
        for feature in record['GBSeq_feature-table']:
            if feature['GBFeature_key'] == 'source':
                if 'GBFeature_qualifiers' in feature:
                    qualifiers = feature['GBFeature_qualifiers']
                    for qualifier in qualifiers:
                        if qualifier['GBQualifier_key'] == 'organelle':
                            organelle = qualifier['GBQualifier_value']

        return taxonomy, organelle

# Example usage
accession = "NM_001301717"  # Replace with your accession number
taxonomy, organelle = fetch_taxonomy_and_organelle(accession)

print(f"Taxonomy: {taxonomy}")
print(f"Organelle: {organelle}")
