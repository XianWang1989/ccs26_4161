
from Bio import Entrez

def fetch_taxonomy_and_organelle(accession):
    # Fetch only the necessary summary data
    Entrez.email = "your_email@example.com"  # Always provide your email
    handle = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text')

    # Read the first few lines to find taxonomy and organelle
    taxonomy = None
    organelle = None

    for line in handle:
        if line.startswith('  ORGANELLE'):
            organelle = line.split(' ')[-1].strip()
        if line.startswith('  '):  # indentation indicates a continuation of an annotation
            if 'taxonomy' in line:
                taxonomy = line.split('taxonomy: ')[-1].strip()

        if taxonomy and organelle:  # Exit early if both values are found
            break

    handle.close()
    return taxonomy, organelle

# Example usage
accession_number = 'YOUR_ACCESSION_NUMBER'
taxonomy, organelle = fetch_taxonomy_and_organelle(accession_number)
print(f'Taxonomy: {taxonomy}, Organelle: {organelle}')
