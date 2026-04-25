
from Bio import SeqIO
from Bio import Entrez

# Function to fetch and extract relevant info
def fetch_taxonomy_and_organelle(accession):
    # Fetching the GenBank record
    response = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text')
    record = SeqIO.read(response, 'genbank')

    # Extract organelle information
    organelle = None
    for feature in record.features:
        if feature.type == 'organelle' and 'organelle' in feature.qualifiers:
            organelle = feature.qualifiers['organelle'][0]
            break

    # Extract taxonomy information
    taxonomy = record.annotations.get('taxonomy', [])

    return {"accession": accession, "organelle": organelle, "taxonomy": taxonomy}

# Example usage
accession_number = "YOUR_ACCESSION_NUMBER"  # replace with your actual accession number
result = fetch_taxonomy_and_organelle(accession_number)

print(result)
