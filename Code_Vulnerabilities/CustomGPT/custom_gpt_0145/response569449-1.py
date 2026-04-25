
from Bio import Entrez
from Bio import SeqIO

# Set your email for Entrez
Entrez.email = "your_email@example.com"

def fetch_and_process_genbank(accession):
    # Fetch the data from NCBI
    handle = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text')

    # Read the record
    record = SeqIO.read(handle, 'genbank')
    handle.close()

    # Extract the organelle feature if available
    organelle = None
    for feature in record.features:
        if feature.type == "organelle":
            organelle = feature.qualifiers.get('organelle', [None])[0]
            break

    # Extract taxonomy information
    taxonomy = record.annotations.get('taxonomy', [])

    return organelle, taxonomy

# Example usage
accession = "YOUR_ACCESSION_NUMBER"
organelle, taxonomy = fetch_and_process_genbank(accession)

if organelle:
    print(f"Organelle: {organelle}")
else:
    print("Organelle feature not found.")

if taxonomy:
    print(f"Taxonomy: {taxonomy}")
else:
    print("Taxonomy information not found.")
