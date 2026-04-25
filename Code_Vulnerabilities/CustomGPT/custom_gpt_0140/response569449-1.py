
from Bio import SeqIO
from Bio import Entrez

Entrez.email = 'your-email@example.com'  # Replace with your email

def fetch_taxonomy_and_organelle(accession):
    # Fetch the GenBank record
    with Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text') as gb_file:
        record = SeqIO.read(gb_file, 'genbank')

        # Extract features relevant to taxonomy and organelle
        taxonomy = record.annotations.get('taxonomy', [])
        organelle = None
        for feature in record.features:
            if 'organelle' in feature.qualifiers:
                organelle = feature.qualifiers['organelle'][0]  # Assuming you want the first entry
                break

        return taxonomy, organelle

# Example usage
accession_numbers = ['NC_000932', 'NC_001416']  # Replace with actual accession numbers
for acc in accession_numbers:
    taxonomy, organelle = fetch_taxonomy_and_organelle(acc)
    if 'Fungi' in taxonomy:
        print(f"{acc} is a fungus with organelle: {organelle}")
