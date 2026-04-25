
from Bio import Entrez
from Bio import SeqIO

# Function to fetch minimal data
def fetch_minimal_genbank_data(accession):
    # Fetch the data directly from NCBI
    handle = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text')
    for record in SeqIO.parse(handle, 'genbank'):
        # Extract only the relevant features
        organelle = None
        if 'organelle' in record.features[0].qualifiers:
            organelle = record.features[0].qualifiers['organelle'][0]
        taxonomy = record.annotations.get('taxonomy', [])
        return organelle, taxonomy
    handle.close()

# Usage example
accessions = ['ABC123', 'DEF456']  # Replace with your accession numbers
for access in accessions:
    organelle, taxonomy = fetch_minimal_genbank_data(access)
    if organelle:
        print(f"Organelle for {access}: {organelle}")
    if taxonomy:
        print(f"Taxonomy for {access}: {taxonomy}")
