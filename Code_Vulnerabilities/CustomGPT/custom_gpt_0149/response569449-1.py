
from Bio import SeqIO
from Bio import Entrez

# Your email here
Entrez.email = "your_email@example.com"

def fetch_taxonomy_and_organelle(accession):
    handle = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text')

    # Parse the GenBank record
    record = SeqIO.read(handle, "genbank")
    handle.close()  # Close the handle after use

    # Retrieve taxonomy
    taxonomy = record.annotations.get('taxonomy', [])

    # Extract organelle information from features
    organelle = None
    for feature in record.features:
        if 'organelle' in feature.qualifiers:
            organelle = feature.qualifiers['organelle'][0]  # Get the first organelle entry
            break

    return taxonomy, organelle

# Example usage
accession_number = "YOUR_ACCESSION_NUMBER"
taxonomy, organelle = fetch_taxonomy_and_organelle(accession_number)

print("Taxonomy:", taxonomy)
print("Organelle:", organelle)
