
from Bio import SeqIO
from Bio import Entrez

# Function to fetch specific information from GenBank
def fetch_genbank_data(accession):
    # Fetching the GenBank entry
    handle = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text')
    # Read only the features of interest
    records = SeqIO.parse(handle, 'genbank')
    for record in records:
        taxonomy = record.annotations.get('taxonomy', [])
        # Check for organelle feature
        organelle = None
        for feature in record.features:
            if 'organelle' in feature.qualifiers:
                organelle = feature.qualifiers['organelle'][0]
                break
        return taxonomy, organelle

# Example usage
accession = 'YOUR_ACCESSION_NUMBER'  # Replace with a valid accession number
taxonomy, organelle = fetch_genbank_data(accession)

print(f'Taxonomy: {taxonomy}')
print(f'Organelle: {organelle}')
