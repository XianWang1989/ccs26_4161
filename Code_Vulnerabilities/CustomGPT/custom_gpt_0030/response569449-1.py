
from Bio import Entrez
from Bio import SeqIO

# Function to fetch only the taxonomy and organelle information
def fetch_taxonomy_and_organelle(accession):
    Entrez.email = "your_email@example.com"  # Always provide your email
    # Fetch summarised information
    handle = Entrez.esummary(db='nucleotide', id=accession)
    record = Entrez.read(handle)[0]

    # Extract taxonomy
    taxonomy = record['Taxonomy']
    # Determine if organelle info is included
    organelle = record.get('Organelle', 'Not mentioned')

    return taxonomy, organelle

# Example usage
accession_number = "YOUR_ACCESSION_NUMBER"
taxonomy, organelle = fetch_taxonomy_and_organelle(accession_number)

# Display the results
print("Taxonomy:", taxonomy)
print("Organelle:", organelle)
