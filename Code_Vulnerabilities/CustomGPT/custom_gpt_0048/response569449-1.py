
from Bio import Entrez
from Bio import SeqIO

# Function to fetch the taxonomy and organelle information
def fetch_taxonomy_organelle(accession):
    try:
        # Fetch the GenBank record
        handle = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text')
        record = SeqIO.read(handle, 'genbank')
        handle.close()

        # Check for organelle information
        organelle = None
        for feature in record.features:
            if feature.type == 'organelle':
                organelle = feature.qualifiers.get('organelle', [None])[0]

        # Get taxonomy info
        taxonomy = record.annotations.get('taxonomy', [])

        return taxonomy, organelle

    except Exception as e:
        print(f"Error fetching data for {accession}: {e}")
        return None, None

# Example usage
accession_list = ['NM_001301717', 'NM_001301718']  # Add your accession numbers here
for access in accession_list:
    taxonomy, organelle = fetch_taxonomy_organelle(access)
    print(f"Accession: {access}, Taxonomy: {taxonomy}, Organelle: {organelle}")
