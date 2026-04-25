
from Bio import Entrez
from Bio import SeqIO

# Function to fetch only necessary features
def fetch_genbank_info(accession):
    Entrez.email = "your_email@example.com"  # Provide your email
    handle = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text')
    record = SeqIO.read(handle, 'genbank')
    handle.close()

    # Extract organelle feature
    organelle = None
    for feature in record.features:
        if feature.type == 'source' and 'organelle' in feature.qualifiers:
            organelle = feature.qualifiers['organelle'][0]
            break

    # Extract taxonomy
    taxonomy = record.annotations.get('taxonomy', [])

    return organelle, taxonomy

# Example usage
accession = "YOUR_ACCESSION_NUMBER"
organelle, taxonomy = fetch_genbank_info(accession)

print("Organelle:", organelle)
print("Taxonomy:", taxonomy)
