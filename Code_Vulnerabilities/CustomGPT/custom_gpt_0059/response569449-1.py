
from Bio import Entrez
from Bio import SeqIO

Entrez.email = "your_email@example.com"  # Your email here
cache = {}

def fetch_taxonomy_and_organelle(accession):
    # Fetch only the necessary data
    handle = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='xml')
    records = SeqIO.parse(handle, 'genbank')

    for record in records:
        # Fetch organelle information
        organelle = None
        for feature in record.features:
            if 'organelle' in feature.qualifiers:
                organelle = feature.qualifiers['organelle'][0]

        # Fetch taxonomy information
        taxonomy = record.annotations['taxonomy'] if 'taxonomy' in record.annotations else []

        # Cache record to avoid re-fetching
        cache[accession] = {
            'organelle': organelle,
            'taxonomy': taxonomy
        }

    handle.close()

# Example usage
accession = "YOUR_ACCESSION_NUMBER"  # Replace this with real accession number
fetch_taxonomy_and_organelle(accession)

# Check the cache
print(cache[accession])
