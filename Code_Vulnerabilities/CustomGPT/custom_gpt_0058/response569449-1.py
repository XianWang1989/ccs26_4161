
from Bio import SeqIO
from Bio import Entrez

def fetch_taxonomy_and_organelle(accession):
    # Fetch the GenBank record once
    with Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text') as gb_file:
        record = SeqIO.read(gb_file, 'genbank')

        # Access the taxonomy
        taxonomy = record.annotations.get('taxonomy', [])
        organelle = None

        # Loop through features to find organelle
        for feature in record.features:
            if 'organelle' in feature.qualifiers:
                organelle = feature.qualifiers['organelle'][0]  # Get the first organelle if available
                break  # Exit after finding the first organelle

        return taxonomy, organelle

# Example usage
accession1 = 'YOUR_ACCESSION_NUMBER_HERE'  # Replace with your accession number
taxonomy, organelle = fetch_taxonomy_and_organelle(accession1)

print("Taxonomy:", taxonomy)
print("Organelle:", organelle if organelle else "Not found")
