
from Bio import Entrez
from Bio import SeqIO

# Function to fetch only necessary parts
def fetch_genbank_part(accession):
    # Fetch data
    with Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text', 
                       rettyp='gb') as handle:
        record = SeqIO.read(handle, 'genbank')

    # Extract organelle
    organelle = None
    for feature in record.features:
        if 'organelle' in feature.qualifiers:
            organelle = feature.qualifiers['organelle'][0]
            break

    # Extract taxonomy
    taxonomy = record.annotations.get('taxonomy', [])

    return organelle, taxonomy

# Example usage
access1 = "YOUR_ACCESSION_NUMBER"
organelle, taxonomy = fetch_genbank_part(access1)

if organelle:
    print(f"Organelle: {organelle}")
if taxonomy:
    print(f"Taxonomy: {taxonomy}")
