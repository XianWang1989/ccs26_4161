
from Bio import SeqIO
from Bio import Entrez

# Function to fetch and extract taxonomy and organelle information
def fetch_taxonomy_organelle(accession):
    Entrez.email = "your_email@example.com"  # Always set your email
    try:
        # Fetch the GenBank record
        gb_record = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text')
        record = SeqIO.read(gb_record, 'genbank')

        # Extract organelle and taxonomy
        organelle = None
        taxonomy = record.annotations.get('taxonomy', [])

        # Check for organelle feature in the record
        for feature in record.features:
            if 'organelle' in feature.qualifiers:
                organelle = feature.qualifiers['organelle'][0]

        return taxonomy, organelle

    except Exception as e:
        print(f"Error processing {accession}: {e}")
        return None, None

# Example usage
accession_number = "YOUR_ACCESSION_NUMBER"  # Replace with your accession number
taxonomy, organelle = fetch_taxonomy_organelle(accession_number)

if taxonomy and organelle:
    print("Taxonomy:", taxonomy)
    print("Organelle:", organelle)
