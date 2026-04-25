
from Bio import Entrez
from Bio import SeqIO

# Function to fetch minimal data from GenBank
def fetch_minimal_genbank_data(accession_id):
    # Use Entrez to fetch the GenBank record
    handle = Entrez.efetch(db='nucleotide', id=accession_id, rettype='gb', retmode='text')

    # Read only the first few lines to extract taxonomy and organelle information
    for line in handle:
        if 'ORGANELLE' in line:
            organelle = line.strip().split(' ')[-1]  # Extract organelle
            break
    else:
        organelle = None  # Default if not found

    # Reset handle to fetch the record for taxonomy
    handle.seek(0)  # Go back to the start of the handle
    taxonomy = None

    for line in handle:
        if line.startswith('  taxonomy'):
            taxonomy = line.strip().split(' ')[1:]  # Extract taxonomy terms
            break

    handle.close()  # Close the handle
    return organelle, taxonomy

# Example usage
accession_id = "ACCESSION_NUMBER"  # Replace with your accession number
organelle, taxonomy = fetch_minimal_genbank_data(accession_id)

if organelle:
    print(f"Organelle: {organelle}")
if taxonomy:
    print(f"Taxonomy: {', '.join(taxonomy)}")
