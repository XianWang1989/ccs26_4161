
from Bio import SeqIO
from Bio import Entrez

def fetch_taxonomy_and_organelle(accession):
    Entrez.email = "your_email@example.com"  # Always set your email
    handle = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text')

    try:
        record = SeqIO.read(handle, 'genbank')

        # Extract organelle if available
        organelle = None
        for feature in record.features:
            if feature.type == "source" and 'organelle' in feature.qualifiers:
                organelle = feature.qualifiers['organelle'][0]
                break

        # Extract taxonomy
        taxonomy = record.annotations.get('taxonomy', [])

        return {
            'accession': accession,
            'taxonomy': taxonomy,
            'organelle': organelle
        }
    finally:
        handle.close()

# Example usage
accession_number = "YOUR_ACCESSION_NUMBER"
data = fetch_taxonomy_and_organelle(accession_number)
print(data)
