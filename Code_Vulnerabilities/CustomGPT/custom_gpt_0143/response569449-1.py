
from Bio import Entrez
from Bio import SeqIO
import io

def fetch_taxonomy_and_organelle(accession):
    # Use Entrez to fetch the GenBank file
    handle = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text')
    gb_record = SeqIO.parse(handle, 'genbank')

    for record in gb_record:
        # Extract taxonomy from annotations
        taxonomy = record.annotations.get('taxonomy', [])
        organelle = None

        # Search for 'organelle' in features
        for feature in record.features:
            if 'organelle' in feature.qualifiers:
                organelle = feature.qualifiers['organelle'][0]  # Get the first organelle entry

        return taxonomy, organelle

# Example usage
accession_number = "YOUR_ACCESSION_NUMBER"
taxonomy, organelle = fetch_taxonomy_and_organelle(accession_number)

# Display results
print(f"Taxonomy: {taxonomy}")
print(f"Organelle: {organelle}")
