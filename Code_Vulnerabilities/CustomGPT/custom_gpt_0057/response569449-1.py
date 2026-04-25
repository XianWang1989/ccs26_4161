
from Bio import Entrez
from Bio import SeqIO

Entrez.email = "your_email@example.com"

def fetch_taxonomy_and_organelle(accession):
    handle = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text')
    record = SeqIO.read(handle, 'genbank')
    handle.close()

    taxonomy = record.annotations.get('taxonomy', [])
    organelle = None

    for feature in record.features:
        if 'organelle' in feature.qualifiers:
            organelle = feature.qualifiers['organelle'][0]
            break

    return taxonomy, organelle

accession_list = ['your_accession_1', 'your_accession_2']  # Replace with your accession numbers
cache = {}

for accession in accession_list:
    taxonomy, organelle = fetch_taxonomy_and_organelle(accession)
    cache[accession] = {'taxonomy': taxonomy, 'organelle': organelle}

# Example output
for acc, data in cache.items():
    print(f"Accession: {acc}, Taxonomy: {data['taxonomy']}, Organelle: {data['organelle']}")
