
from Bio import SeqIO
from Bio import Entrez

# Function to fetch and extract relevant information from GenBank records.
def fetch_genbank_info(accession):
    try:
        # Fetch the GenBank record
        with Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text') as gb_file:
            # Parse the GenBank record
            record = SeqIO.read(gb_file, 'genbank')

        # Extract the taxonomy
        taxonomy = record.annotations.get('taxonomy', [])
        organelle = None

        # Check features for organelle information
        for feature in record.features:
            if 'organelle' in feature.qualifiers:
                organelle = feature.qualifiers['organelle'][0]
                break

        return {'taxonomy': taxonomy, 'organelle': organelle}

    except Exception as e:
        print(f"Error fetching or parsing {accession}: {e}")
        return None

# Example usage
accession_list = ['ACCESSION_1', 'ACCESSION_2']  # Replace with actual accession numbers
results = {}

for acc in accession_list:
    result = fetch_genbank_info(acc)
    if result:
        results[acc] = result

# Now the `results` dictionary holds the taxonomy and organelle for each accession.
