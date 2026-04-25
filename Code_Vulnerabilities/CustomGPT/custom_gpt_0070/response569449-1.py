
from Bio import SeqIO
from Bio import Entrez

# Set your email to use NCBI Entrez
Entrez.email = "your_email@example.com"

# Define function to fetch and extract information
def fetch_gb_info(accession):
    # Fetch the GenBank record
    with Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text') as handle:
        # Read the record
        record = SeqIO.read(handle, 'genbank')

        # Extract organelle, if available
        organelle = None
        for feature in record.features:
            if feature.type == "source" and 'organelle' in feature.qualifiers:
                organelle = feature.qualifiers['organelle'][0]
                break

        # Extract taxonomy
        taxonomy = record.annotations.get('taxonomy', [])

        return organelle, taxonomy

# Example usage
accession_numbers = ['ACCESSION1', 'ACCESSION2']  # Replace with your accession numbers
for accession in accession_numbers:
    organelle, taxonomy = fetch_gb_info(accession)
    print(f'Accession: {accession}\nOrganelle: {organelle}\nTaxonomy: {taxonomy}\n')
