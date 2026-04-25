
from Bio import SeqIO
from Bio import Entrez

# Function to fetch minimal information from GenBank using accession number
def fetch_minimal_genbank_info(accession):
    # Fetch the GenBank record
    handle = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text')
    record = SeqIO.read(handle, 'genbank')
    handle.close()

    # Extract taxonomy and organelle
    taxonomy = record.annotations.get('taxonomy', [])
    organelle = next((feat for feat in record.features if 'organelle' in feat.qualifiers), None)

    return taxonomy, organelle

# Usage example
accession_number = "YOUR_ACCESSION_HERE"
taxonomy, organelle = fetch_minimal_genbank_info(accession_number)

# Process the results
if taxonomy:
    print("Taxonomy:", taxonomy)
if organelle:
    print("Organelle:", organelle.qualifiers['organelle'])
