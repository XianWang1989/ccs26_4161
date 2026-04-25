
from Bio import Entrez
from Bio import SeqIO

# Function to fetch taxonomy and organelle information
def fetch_genbank_info(accession):
    # Fetching the data in XML format
    handle = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='xml')
    records = SeqIO.parse(handle, 'genbank')

    for record in records:
        # Extracting taxonomy
        taxonomy = record.annotations.get('taxonomy', [])
        organelle = None

        # Searching for organelle in features
        for feat in record.features:
            if 'organelle' in feat.qualifiers:
                organelle = feat.qualifiers['organelle'][0]
                break

        # Return desired information
        return {"taxonomy": taxonomy, "organelle": organelle}

# Example usage
accession_number = "YOUR_ACCESSION_NUMBER"  # Replace with your accession number
info = fetch_genbank_info(accession_number)

if info:
    print(f"Taxonomy: {info['taxonomy']}")
    print(f"Organelle: {info['organelle']}")
