
from Bio import SeqIO
from Bio import Entrez

# Ensure you have set your email for Entrez usage
Entrez.email = "your_email@example.com"

def fetch_genbank_data(accession):
    try:
        # Fetch the GenBank record
        with Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text') as gb_file:
            # Parse the GenBank record
            record = SeqIO.read(gb_file, 'genbank')
            # Extract taxonomy
            taxonomy = record.annotations.get('taxonomy', [])
            # Extract organelle, if present
            organelle = None
            for feature in record.features:
                if 'organelle' in feature.qualifiers:
                    organelle = feature.qualifiers['organelle'][0]
                    break

            return taxonomy, organelle

    except Exception as e:
        print(f"Error fetching {accession}: {e}")
        return None, None

# Example usage
accession_numbers = ["NC_000852", "NC_001301"]  # Example accession numbers
results = {}

for acc in accession_numbers:
    taxonomy, organelle = fetch_genbank_data(acc)
    if taxonomy and organelle:
        results[acc] = {
            "taxonomy": taxonomy,
            "organelle": organelle,
        }

print(results)
