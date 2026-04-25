
from Bio import Entrez
from Bio import SeqIO

# Function to fetch minimal information from a GenBank record
def fetch_genbank_info(accession):
    Entrez.email = "your_email@example.com"  # Always provide your email
    handle = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text')
    record = SeqIO.read(handle, 'genbank')
    handle.close()

    # Extract only the relevant information
    taxonomy = record.annotations.get('taxonomy', [])
    organelle = None

    # Loop through features to find the organelle
    for feature in record.features:
        if 'organelle' in feature.qualifiers:
            organelle = feature.qualifiers['organelle'][0]
            break

    return taxonomy, organelle

# Example usage
accession_number = "YOUR_ACCESSION_NUMBER"
taxonomy, organelle = fetch_genbank_info(accession_number)

print("Taxonomy:", taxonomy)
print("Organelle:", organelle)
