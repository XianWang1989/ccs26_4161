
from Bio import Entrez
from Bio import SeqIO

# Function to fetch and extract the required information
def fetch_genbank_info(access):
    # Fetch only the summary of the GenBank record
    handle = Entrez.efetch(db='nucleotide', id=access, rettype='gb', retmode='text', dbfrom='nucleotide')

    # Read the GenBank record
    record = SeqIO.read(handle, 'genbank')

    # Close the handle
    handle.close()

    # Extract taxonomy
    taxonomy = record.annotations.get('taxonomy', [])

    # Extract organelle
    organelle = None
    for feature in record.features:
        if 'organelle' in feature.qualifiers:
            organelle = feature.qualifiers['organelle'][0]  # Assuming you want the first organelle

    return taxonomy, organelle

# Example accession number
access1 = "YOUR_ACCESSION_NUMBER"

# Usage of the function
taxonomy, organelle = fetch_genbank_info(access1)

# Example checks
if 'Fungi' in taxonomy:  # Check taxonomy
    print(f"The organism is a Fungi.")
if organelle:  # Check organelle
    print(f"The organelle of the organism is: {organelle}")
