
from Bio import SeqIO
from Bio import Entrez

# Function to fetch necessary details from GenBank
def fetch_genbank_data(accession):
    try:
        # Fetch the GenBank record
        gb_handle = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text')
        record = SeqIO.read(gb_handle, 'genbank')

        # Extract organelle information if available
        organelle = None
        for feature in record.features:
            if 'organelle' in feature.qualifiers:
                organelle = feature.qualifiers['organelle'][0]

        # Extract taxonomy information
        taxonomy = record.annotations.get('taxonomy', [])

        return organelle, taxonomy

    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None

# Example usage
accession_number = "YOUR_ACCESSION_NUMBER"
organelle, taxonomy = fetch_genbank_data(accession_number)

if organelle:
    print(f"Organelle: {organelle}")
if taxonomy:
    print(f"Taxonomy: {taxonomy}")
