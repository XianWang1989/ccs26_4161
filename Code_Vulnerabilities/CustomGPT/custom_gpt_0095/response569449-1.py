
from Bio import Entrez, SeqIO

# Function to get taxonomy and organelle
def fetch_taxonomy_and_organelle(accession):
    Entrez.email = "your_email@example.com"  # Always provide your email
    handle = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text')
    record = SeqIO.read(handle, 'genbank')
    handle.close()

    # Extract taxonomy
    taxonomy = record.annotations.get('taxonomy', [])
    organelle = None

    # Look for organelle in the features
    for feature in record.features:
        if 'organelle' in feature.qualifiers:
            organelle = feature.qualifiers['organelle'][0]
            break

    return taxonomy, organelle

# Example use
accession_number = "Access_Your_Accession_Number"
taxonomy, organelle = fetch_taxonomy_and_organelle(accession_number)

print("Taxonomy:", taxonomy)
print("Organelle:", organelle)
