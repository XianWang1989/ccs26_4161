
from Bio import SeqIO
from Bio import Entrez

# Always provide your email to NCBI
Entrez.email = "your_email@example.com"

# Function to get taxonomy and organelle information
def get_genbank_info(access):
    # Fetch the GenBank record
    handle = Entrez.efetch(db='nucleotide', id=access, rettype='gb', retmode='text')
    record = SeqIO.read(handle, 'genbank')
    handle.close()

    # Extracting taxonomy
    taxonomy = record.annotations.get('taxonomy', [])
    organelle = None

    # Check for organelle feature
    for feature in record.features:
        if 'organelle' in feature.qualifiers:
            organelle = feature.qualifiers['organelle'][0]
            break

    return taxonomy, organelle

# Example usage
accession_numbers = ["ACCESSION1", "ACCESSION2"]  # Replace with your accession numbers
fungi_count = 0

for access in accession_numbers:
    taxonomy, organelle = get_genbank_info(access)

    if taxonomy and taxonomy[1] == 'Fungi':
        fungi_count += 1

# Output the results
print(f"Number of fungi: {fungi_count}")
