
from Bio import SeqIO
from Bio import Entrez

def fetch_genbank_data(accession):
    # Fetch the data in GenBank format
    handle = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text')
    record = SeqIO.read(handle, 'genbank')
    handle.close()
    return record

def extract_taxonomy_and_organelle(accession):
    record = fetch_genbank_data(accession)

    # Extract taxonomy
    taxonomy = record.annotations.get('taxonomy', [])
    organelle = None

    # Check for organelle in features
    for feature in record.features:
        if 'organelle' in feature.qualifiers:
            organelle = feature.qualifiers['organelle'][0]
            break

    return taxonomy, organelle

# Example usage
accession_number = 'YOUR_ACCESSION_NUMBER'  # Replace with your actual accession number
taxonomy, organelle = extract_taxonomy_and_organelle(accession_number)

print("Taxonomy:", taxonomy)
print("Organelle:", organelle)
