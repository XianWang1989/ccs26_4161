
from Bio import SeqIO
from Bio import Entrez

def fetch_genbank_part(accession):
    # Fetch GenBank entry
    with Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text') as gb_file:
        # Read the record
        record = SeqIO.read(gb_file, 'genbank')

        # Extract taxonomy
        taxonomy = record.annotations.get('taxonomy', [])
        organelle = None

        # Check for organelle feature
        for feature in record.features:
            if 'organelle' in feature.qualifiers:
                organelle = feature.qualifiers['organelle']
                break

        return taxonomy, organelle

# Example usage
accession_number = "YOUR_ACCESSION_NUMBER"  # Replace with your accession number
taxonomy, organelle = fetch_genbank_part(accession_number)

print("Taxonomy:", taxonomy)
print("Organelle:", organelle)
