
from Bio import Entrez

# Always provide your email
Entrez.email = "your_email@example.com"

def fetch_taxonomy_and_organelle(accession):
    # Fetch the GenBank record
    handle = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text')

    # Read only the relevant parts of the record
    record = handle.read()

    # Check for taxonomy
    taxonomy_start = record.find("taxonomy")
    taxonomy_end = record.find("\n", taxonomy_start)
    taxonomy = record[taxonomy_start:taxonomy_end].strip().split()[1:]  # Get the taxonomy list

    # Check for organelle (if available)
    organelle = None
    if "organelle" in record:
        organelle_start = record.find("organelle")
        organelle_end = record.find("\n", organelle_start)
        organelle = record[organelle_start:organelle_end].strip().split()[1]  # Get the organelle info

    return taxonomy, organelle

# Example usage
accessions = ["YOUR_ACCESSION_NUMBER"]
for acc in accessions:
    taxonomy, organelle = fetch_taxonomy_and_organelle(acc)

    if 'Fungi' in taxonomy:
        print(f"{acc}: Found Fungi in taxonomy.")

    if organelle:
        print(f"{acc}: Found organelle information: {organelle}")
