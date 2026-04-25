
from Bio import Entrez
from Bio import SeqIO

# Function to fetch minimal data
def fetch_taxonomy_and_organelle(accession):
    # Fetch the GenBank record using the accession number
    handle = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text')

    # Read record without loading everything into memory
    record = SeqIO.read(handle, 'genbank')
    handle.close()

    # Extracting taxonomy
    taxonomy = record.annotations.get('taxonomy', [])

    # Check organelle from features if available
    organelle = None
    for feature in record.features:
        if 'organelle' in feature.qualifiers:
            organelle = feature.qualifiers['organelle'][0]
            break

    return taxonomy, organelle

# Example usage
accessions = ['access1', 'access2']  # replace with your actual accession numbers
for acc in accessions:
    taxonomy, organelle = fetch_taxonomy_and_organelle(acc)
    print(f"Accession: {acc}, Taxonomy: {taxonomy}, Organelle: {organelle}")
