
from Bio import SeqIO
from Bio import Entrez

def fetch_taxonomy_and_organelle(accession):
    Entrez.email = "your_email@example.com"  # Always set your email
    handle = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text')

    # Parse the specific fields we need
    for record in SeqIO.parse(handle, 'genbank'):
        taxonomy = record.annotations.get('taxonomy', [])
        organelle_feature = next((f for f in record.features if f.type == 'organelle'), None)

        organelle = organelle_feature.qualifiers['organelle'][0] if organelle_feature else None

        return taxonomy, organelle

    handle.close()
    return None, None

# Example usage
accession_number = "YOUR_ACCESSION_NUMBER"
taxonomy, organelle = fetch_taxonomy_and_organelle(accession_number)

if taxonomy:
    print(f"Taxonomy: {taxonomy}")
if organelle:
    print(f"Organelle: {organelle}")
