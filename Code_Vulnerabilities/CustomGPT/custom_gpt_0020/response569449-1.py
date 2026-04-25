
from Bio import SeqIO
from Bio import Entrez

# Function to fetch relevant features from the GenBank entry
def fetch_relevant_features(access):
    # Fetch the GenBank entry
    try:
        gb_file = Entrez.efetch(db='nucleotide', id=access, rettype='gb', retmode='text')
        rec = SeqIO.read(gb_file, 'genbank')

        # Extract taxonomy
        taxonomy = rec.annotations.get('taxonomy', [])
        organelle = None

        # Check for organelle in features
        for feat in rec.features:
            if 'organelle' in feat.qualifiers:
                organelle = feat.qualifiers['organelle'][0]
                break

        return taxonomy, organelle
    except Exception as e:
        print(f"An error occurred while fetching {access}: {e}")
        return None, None

# Replace with your accession number list
accession_numbers = ['ACCESSION1', 'ACCESSION2']

for access in accession_numbers:
    taxonomy, organelle = fetch_relevant_features(access)

    if taxonomy:
        print(f"{access} - Taxonomy: {taxonomy}")
    if organelle:
        print(f"{access} - Organelle: {organelle}")
