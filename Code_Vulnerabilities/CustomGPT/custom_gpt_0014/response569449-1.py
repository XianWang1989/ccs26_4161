
from Bio import Entrez
from Bio import SeqIO

def fetch_genbank_metadata(accession):
    Entrez.email = "your_email@example.com"  # Always provide your email
    # Fetch the GenBank data in text format
    handle = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text')

    # Read the record
    record = SeqIO.read(handle, 'genbank')
    handle.close()

    # Extract relevant information
    organelle = None
    taxonomy = record.annotations.get('taxonomy', [])

    for feature in record.features:
        if 'organelle' in feature.qualifiers:
            organelle = feature.qualifiers['organelle'][0]
            break  # Exit early if we find the organelle

    return taxonomy, organelle

# Example usage
accession_list = ['accession1', 'accession2']  # Replace with your accession numbers
results = {}

for acc in accession_list:
    taxonomy, organelle = fetch_genbank_metadata(acc)
    results[acc] = {'taxonomy': taxonomy, 'organelle': organelle}

# Print results
for acc, data in results.items():
    print(f"Accession: {acc}, Taxonomy: {data['taxonomy']}, Organelle: {data['organelle']}")
