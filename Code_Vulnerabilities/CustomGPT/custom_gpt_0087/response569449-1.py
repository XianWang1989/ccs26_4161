
from Bio import SeqIO
from Bio import Entrez

# Setup your Entrez email
Entrez.email = "your_email@example.com"

# Function to fetch specific information from GenBank
def fetch_genbank_info(access_id):
    try:
        # Fetch the record
        with Entrez.efetch(db='nucleotide', id=access_id, rettype='gb', retmode='text') as handle:
            record = SeqIO.read(handle, 'genbank')

        # Extract organelle information
        organelle = None
        for feature in record.features:
            if 'organelle' in feature.qualifiers.keys():
                organelle = feature.qualifiers['organelle'][0]

        # Extract taxonomy information
        taxonomy = record.annotations.get('taxonomy', [])

        return organelle, taxonomy

    except Exception as e:
        print(f"Error fetching data for {access_id}: {e}")
        return None, None

# Example usage
access1 = "YOUR_ACCESSION_NUMBER"  # Replace with your accession number
organelle, taxonomy = fetch_genbank_info(access1)

if organelle:
    print(f"Organelle: {organelle}")
if taxonomy:
    print(f"Taxonomy: {taxonomy}")
