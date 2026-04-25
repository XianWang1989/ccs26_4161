
from Bio import SeqIO
from Bio import Entrez

# Initialize your Entrez email
Entrez.email = "your_email@example.com"

def fetch_organism_info(accession):
    # Fetch the record
    with Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text') as gb_file:
        # Read the GenBank record
        rec = SeqIO.read(gb_file, 'genbank')

    # Extract the organelle if available
    organelle = None
    for feat in rec.features:
        if feat.type == "source" and 'organelle' in feat.qualifiers:
            organelle = feat.qualifiers['organelle'][0]
            break

    # Extract taxonomy
    taxonomy = rec.annotations.get('taxonomy', [])

    return organelle, taxonomy

# Example usage
accession_number = "NC_000852"  # Replace with your accession number
organelle, taxonomy = fetch_organism_info(accession_number)

print(f"Organelle: {organelle}")
print(f"Taxonomy: {taxonomy}")
