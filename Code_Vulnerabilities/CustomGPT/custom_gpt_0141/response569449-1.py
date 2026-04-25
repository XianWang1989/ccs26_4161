
from Bio import SeqIO
from Bio import Entrez

# Ensure you have your email set for Entrez
Entrez.email = "your_email@example.com"  # Replace with your email

def fetch_taxonomy_and_organelle(accession):
    # Fetch GenBank record but only the text for quick parse
    handle = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text', seq_start=1, seq_stop=10)

    # Read the record
    rec = SeqIO.read(handle, 'genbank')
    handle.close()

    # Extract the required information
    taxonomies = rec.annotations.get('taxonomy', [])
    organelle = None

    # Loop through the features to find organelle
    for feature in rec.features:
        if 'organelle' in feature.qualifiers:
            organelle = feature.qualifiers['organelle'][0]  # Take the first organelle if multiple are present
            break

    return taxonomies, organelle

# Example usage
accession_numbers = ['ACCESSION1', 'ACCESSION2']  # Replace with actual accession numbers
for access in accession_numbers:
    taxonomy, organelle = fetch_taxonomy_and_organelle(access)
    print(f"Accession: {access}, Taxonomy: {taxonomy}, Organelle: {organelle}")
