
from Bio import SeqIO
from Bio import Entrez

# Function to fetch only necessary parts of the GenBank record
def fetch_taxonomy_and_organelle(accession):
    # Fetch the GenBank record
    gb_record = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text')
    record = SeqIO.read(gb_record, 'genbank')

    # Extract taxonomy
    taxonomy = record.annotations.get('taxonomy', [])
    organelle = None

    # Check for organelle feature
    for feature in record.features:
        if feature.type == 'source' and 'organelle' in feature.qualifiers:
            organelle = feature.qualifiers['organelle'][0]
            break

    return taxonomy, organelle

# Example usage
Entrez.email = "your_email@example.com"  # Always provide your email
accession_numbers = ['ACCESSION_1', 'ACCESSION_2']  # replace with your accession numbers
results = {}

for accession in accession_numbers:
    taxonomy, organelle = fetch_taxonomy_and_organelle(accession)
    results[accession] = {
        'taxonomy': taxonomy,
        'organelle': organelle
    }

# Display results
print(results)
