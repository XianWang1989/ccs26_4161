
from Bio import SeqIO
from Bio import Entrez

# Function to fetch minimal details from GenBank
def fetch_genbank_info(accession):
    # Fetch the GenBank record
    handle = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text')
    # Parse the GenBank record
    record = SeqIO.read(handle, 'genbank')
    handle.close()

    # Extract the organelle if available
    organelle = None
    for feature in record.features:
        if 'organelle' in feature.qualifiers:
            organelle = feature.qualifiers['organelle'][0]
            break

    # Extract taxonomy
    taxonomy = record.annotations.get('taxonomy', [])

    return organelle, taxonomy

# Example usage
accession = "Your_Accession_Number"
organelle, taxonomy = fetch_genbank_info(accession)

if organelle:
    print(f"Organelle: {organelle}")
if taxonomy:
    print(f"Taxonomy: {taxonomy}")
