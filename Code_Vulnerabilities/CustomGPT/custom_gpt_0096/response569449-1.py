
from Bio import Entrez
from Bio import SeqIO

Entrez.email = "your_email@example.com"  # Always include your email

def fetch_taxo_organelle(accession):
    # Fetch the GenBank record
    with Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text') as gb_file:
        # Parse the GenBank record
        record = SeqIO.read(gb_file, 'genbank')

        # Extract taxonomy
        taxonomy = record.annotations.get('taxonomy', [])
        # Extract organelle information if available in features
        organelle = None
        for feature in record.features:
            if 'organelle' in feature.qualifiers:
                organelle = feature.qualifiers['organelle'][0]

        return taxonomy, organelle

# Example usage
accession_number = "YOUR_ACCESSION_NUMBER"
taxonomy, organelle = fetch_taxo_organelle(accession_number)

print(f"Taxonomy: {taxonomy}")
print(f"Organelle: {organelle}")
