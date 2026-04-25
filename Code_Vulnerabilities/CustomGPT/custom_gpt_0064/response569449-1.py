
from Bio import SeqIO
from Bio import Entrez

# Initialize Entrez email
Entrez.email = "your_email@example.com"

def fetch_genbank_info(accession):
    # Fetch the GenBank record using efetch
    gb_record = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text')

    # Read the GenBank record
    record = SeqIO.read(gb_record, 'genbank')

    # Extract taxonomy
    taxonomy = record.annotations.get('taxonomy', [])

    # Check for organelle
    organelle_info = None
    for feature in record.features:
        if 'organelle' in feature.qualifiers:
            organelle_info = feature.qualifiers['organelle'][0]
            break

    return taxonomy, organelle_info

# Example of fetching for a list of accessions
accessions = ['ACCESSION_NUMBER_1', 'ACCESSION_NUMBER_2']
for acc in accessions:
    taxonomy, organelle = fetch_genbank_info(acc)
    print(f"Taxonomy: {taxonomy}, Organelle: {organelle}")
