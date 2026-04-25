
from Bio import Entrez
from Bio import SeqIO

# Function to fetch only the organelle and taxonomy
def fetch_genbank_info(accession):
    Entrez.email = "your_email@example.com"  # Replace with your email
    handle = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text')

    # Read the GenBank record
    record = SeqIO.read(handle, 'genbank')

    # Extract organelle if available
    organelle = None
    for feature in record.features:
        if feature.type == 'source' and 'organelle' in feature.qualifiers:
            organelle = feature.qualifiers['organelle'][0]
            break

    # Extract taxonomy
    taxonomy = record.annotations['taxonomy'] if 'taxonomy' in record.annotations else []

    return organelle, taxonomy

# Example usage
accession_number = "YOUR_ACCESSION_HERE"  # Replace with an actual accession number
organelle, taxonomy = fetch_genbank_info(accession_number)

print(f"Organelle: {organelle}")
print(f"Taxonomy: {taxonomy}")
