
from Bio import SeqIO
from Bio import Entrez

# Set your email (required by NCBI)
Entrez.email = "your_email@example.com"

def fetch_genbank_info(accession):
    # Fetch the GenBank record
    with Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text') as gb_file:
        record = SeqIO.read(gb_file, 'genbank')

        # Extract taxonomy
        taxonomy = record.annotations.get('taxonomy', [])
        organelle = None

        # Look for the organelle feature
        for feature in record.features:
            if 'organelle' in feature.qualifiers:
                organelle = feature.qualifiers['organelle'][0]
                break

        return taxonomy, organelle

# Example usage
accession_list = ['ACCESSION_1', 'ACCESSION_2']  # Replace with actual accession numbers
results = {}

for access in accession_list:
    taxonomy, organelle = fetch_genbank_info(access)
    results[access] = {'taxonomy': taxonomy, 'organelle': organelle}

print(results)
