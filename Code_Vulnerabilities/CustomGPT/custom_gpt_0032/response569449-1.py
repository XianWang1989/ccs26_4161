
from Bio import SeqIO
from Bio import Entrez

Entrez.email = "your_email@example.com"  # Always set your email

def fetch_taxonomy_and_organelle(accession):
    # Fetch the GenBank record
    with Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text') as gb_handle:
        # Read the record
        for record in SeqIO.parse(gb_handle, 'genbank'):
            # Get the taxonomy
            taxonomy = record.annotations.get('taxonomy', [])
            organelle = None

            # Check for organelle in features
            for feature in record.features:
                if 'organelle' in feature.qualifiers:
                    organelle = feature.qualifiers['organelle'][0]
                    break

            return taxonomy, organelle

# Example usage
accession = "NC_000852"  # Example accession number
taxonomy, organelle = fetch_taxonomy_and_organelle(accession)
print(f'Taxonomy: {taxonomy}')
print(f'Orgel: {organelle}')
