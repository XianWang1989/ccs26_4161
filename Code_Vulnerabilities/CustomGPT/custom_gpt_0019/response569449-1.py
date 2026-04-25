
from Bio import Entrez
from Bio import SeqIO

def fetch_genbank_info(accession):
    Entrez.email = "your_email@example.com"  # Always include your email
    handle = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text')
    record = SeqIO.read(handle, 'genbank')
    handle.close()

    # Extract organelle
    organelle_info = None
    for feature in record.features:
        if 'organelle' in feature.qualifiers:
            organelle_info = feature.qualifiers['organelle'][0]
            break

    # Extract taxonomy
    taxonomy_info = record.annotations.get('taxonomy', [])

    return {
        'accession': accession,
        'organelle': organelle_info,
        'taxonomy': taxonomy_info
    }

# Example usage
accession_number = "NC_001416"  # Replace with your accession number
data = fetch_genbank_info(accession_number)
print(data)
