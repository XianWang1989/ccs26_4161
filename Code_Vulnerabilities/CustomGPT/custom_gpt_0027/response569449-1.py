
from Bio import Entrez
from Bio import SeqIO

def fetch_taxonomy_and_organelle(accession):
    Entrez.email = "your_email@example.com"  # Always include your email
    handle = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text')

    for record in SeqIO.parse(handle, 'genbank'):
        # Get the taxonomy
        taxonomy = record.annotations.get('taxonomy', [])
        organelle = None

        # Check for organelle in features
        for feature in record.features:
            if 'organelle' in feature.qualifiers:
                organelle = feature.qualifiers['organelle'][0]

        # Process taxonomy and organelle as needed
        print(f"Accession: {accession}")
        print(f"Taxonomy: {taxonomy}")
        if organelle:
            print(f"Organelle: {organelle}")
        else:
            print("Organelle: Not found")

    handle.close()

# Example usage
accession_number = "YOUR_ACCESSION_NUMBER"
fetch_taxonomy_and_organelle(accession_number)
