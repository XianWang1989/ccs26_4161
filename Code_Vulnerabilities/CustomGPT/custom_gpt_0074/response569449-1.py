
from Bio import SeqIO
from Bio import Entrez

Entrez.email = 'your_email@example.com'  # Always set your email when using Entrez

def fetch_genbank_data(accession):
    # Fetch the GenBank record
    try:
        gb_handle = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text')
        record = SeqIO.read(gb_handle, 'genbank')

        # Extracting taxonomy
        taxonomy = record.annotations.get('taxonomy', [])
        organelle_info = ""

        # Searching for the organelle feature
        for feature in record.features:
            if 'organelle' in feature.qualifiers:
                organelle_info = feature.qualifiers['organelle'][0]
                break  # Exit the loop once you find the organelle information

        return {
            'taxonomy': taxonomy,
            'organelle': organelle_info
        }

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
accession_number = "YOUR_ACCESSION_NUMBER"  # Replace with your actual accession number
data = fetch_genbank_data(accession_number)

if data:
    print(f"Taxonomy: {data['taxonomy']}")
    print(f"Organelle: {data['organelle']}")
