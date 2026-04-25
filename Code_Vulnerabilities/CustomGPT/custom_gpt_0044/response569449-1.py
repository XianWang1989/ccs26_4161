
from Bio import Entrez
from Bio import SeqIO

Entrez.email = "your_email@example.com"  # Always provide your email

def fetch_taxonomy_and_organelle(accession):
    # Fetch summary information
    handle = Entrez.esummary(db='nucleotide', id=accession)
    record = Entrez.read(handle)[0]

    # Retrieve taxonomy and organelle if available
    taxonomy = record.get("Taxonomy", [])
    organelle = record.get("Organelle", None)

    return taxonomy, organelle

# Example of usage
access1 = "YOUR_ACCESSION_NUMBER"
taxonomy, organelle = fetch_taxonomy_and_organelle(access1)

if taxonomy and "Fungi" in taxonomy:  # Check taxonomy
    fungi_count += 1

# You can access organelle if needed
if organelle:
    # Do something with organelle information
    print(f"Organelle: {organelle}")
