
from Bio import SeqIO
from Bio import Entrez

# Your Entrez email here
Entrez.email = "your_email@example.com"

def fetch_taxonomy_and_organelle(accession):
    try:
        # Fetch the GenBank record
        gb_handle = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text')
        # Parse the GenBank file directly
        record = SeqIO.read(gb_handle, 'genbank')

        # Extract taxonomy
        taxonomy = record.annotations.get('taxonomy', [])
        organelle = None

        # Check for organelle in features
        for feature in record.features:
            if feature.type == 'gene' and 'organelle' in feature.qualifiers:
                organelle = feature.qualifiers['organelle'][0]
                break  # Stop once we find the first organelle feature

        return {
            'taxonomy': taxonomy,
            'organelle': organelle
        }

    except Exception as e:
        print(f"An error occurred while fetching the accession {accession}: {e}")
        return None

# Example usage
accession = "NC_001416"  # Replace with the actual accession number
result = fetch_taxonomy_and_organelle(accession)

if result:
    print(f"Taxonomy: {result['taxonomy']}")
    print(f"Organelle: {result['organelle']}")
