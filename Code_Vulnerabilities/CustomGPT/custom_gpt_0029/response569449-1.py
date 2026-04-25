
from Bio import Entrez

# Function to fetch taxonomy and organelle from a GenBank accession
def fetch_taxonomy_and_organelle(accession):
    Entrez.email = "your_email@example.com"  # Provide your email
    # Fetch only the header information
    handle = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text', seq_start=1, seq_stop=1)

    # Read the record
    record = handle.read()
    handle.close()

    # Extract taxonomy
    lines = record.splitlines()
    taxonomy = None
    organelle = None

    for line in lines:
        if line.startswith("ORGANISM"):
            organelle = line.split()[1]  # Adjust parsing as needed
        if line.startswith("SOURCE"):
            taxonomy = line.replace("SOURCE", "").strip()

    return taxonomy, organelle

# Example usage:
accessions = ['NC_001477', 'NC_001481']  # Add your accession numbers
for acc in accessions:
    taxonomy, organelle = fetch_taxonomy_and_organelle(acc)
    print(f'Accession: {acc}, Taxonomy: {taxonomy}, Organelle: {organelle}')
