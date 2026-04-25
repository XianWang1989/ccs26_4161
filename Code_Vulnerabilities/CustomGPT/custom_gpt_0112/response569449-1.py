
from Bio import SeqIO
from Bio import Entrez

Entrez.email = "your_email@example.com"  # Always provide your email

def fetch_genbank_info(accession):
    # Fetch the GenBank record with minimal data
    handle = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text')

    # Parse the record
    record = SeqIO.read(handle, 'genbank')
    handle.close()  # Always close the handle

    # Extract organelle if available
    organelle = None
    for feature in record.features:
        if 'organelle' in feature.qualifiers:
            organelle = feature.qualifiers['organelle'][0]
            break

    # Get taxonomy
    taxonomy = record.annotations.get('taxonomy', [])

    return taxonomy, organelle

# Example usage
accession_number = 'YOUR_ACCESSION_NUMBER'  # replace with the actual accession number
taxonomy_info, organelle_info = fetch_genbank_info(accession_number)

print("Taxonomy:", taxonomy_info)
print("Organelle:", organelle_info)
