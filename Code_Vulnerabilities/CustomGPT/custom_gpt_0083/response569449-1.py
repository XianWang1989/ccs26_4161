
from Bio import SeqIO
from Bio import Entrez

# Your Entrez email
Entrez.email = "your_email@example.com"

# Function to fetch taxonomy and organelle
def fetch_taxonomy_and_organelle(accession):
    # Fetch the GenBank record
    with Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text') as gb_file:
        # Parse the record
        record = SeqIO.read(gb_file, 'genbank')

        # Extract organelle information
        organelle = None
        for feature in record.features:
            if feature.type == "organelle" and 'organelle' in feature.qualifiers:
                organelle = feature.qualifiers['organelle'][0]
                break

        # Extract taxonomy information
        taxonomy = record.annotations.get('taxonomy', [])

        return {
            'accession': accession,
            'organelle': organelle,
            'taxonomy': taxonomy
        }

# Example usage
accession_list = ["ACCESSION_1", "ACCESSION_2"]  # Replace with actual accession numbers
results = {}

for accession in accession_list:
    results[accession] = fetch_taxonomy_and_organelle(accession)

# Output the results
print(results)
