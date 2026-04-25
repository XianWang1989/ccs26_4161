
from Bio import Entrez

# Function to fetch taxonomy and organelle
def fetch_taxonomy_and_organelle(accession):
    Entrez.email = "your_email@example.com"  # Replace with your email
    # Fetch summary of the GenBank record
    handle = Entrez.esummary(db='nucleotide', id=accession)
    records = Entrez.read(handle)

    # Extracting relevant information
    for record in records:
        taxonomy = record.get('Taxonomy', 'Not available')
        organelle = record.get('Organelle', 'Not available')

        # Process the extracted information
        if 'Fungi' in taxonomy:
            fungi_count = 1  # Or any processing you want to do

        print(f"Accession: {accession}, Taxonomy: {taxonomy}, Organelle: {organelle}")

    handle.close()

# Example usage
accession_number = "NC_001301"  # Replace with your accession number
fetch_taxonomy_and_organelle(accession_number)
