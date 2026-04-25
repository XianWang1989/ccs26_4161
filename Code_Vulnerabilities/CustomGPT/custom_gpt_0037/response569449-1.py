
from Bio import Entrez

Entrez.email = "your_email@example.com"  # Always include your email

def fetch_taxonomy_and_organelle(access1):
    # Fetch summary information for the accession number
    handle = Entrez.esummary(db='nucleotide', id=access1, retmode='xml')
    records = Entrez.read(handle)
    handle.close()

    # Extract taxonomy
    taxonomy = records[0]['Taxonomy']

    # For organelle, we can only retrieve features if we still need to,
    # since esummary doesn't provide detailed features.
    organelle = None  # Default if not found

    # If organelle is critical, you may need to fetch features separately 
    # as there's no direct way to get it from the summary.
    handle = Entrez.efetch(db='nucleotide', id=access1, rettype='gb', retmode='text')
    for record in SeqIO.parse(handle, 'genbank'):
        for feature in record.features:
            if 'organelle' in feature.qualifiers:
                organelle = feature.qualifiers['organelle'][0]
                break
    handle.close()

    return taxonomy, organelle

access1 = "YOUR_ACCESSION_NUMBER"  # Replace with your accession number
taxonomy, organelle = fetch_taxonomy_and_organelle(access1)

print(f'Taxonomy: {taxonomy}')
print(f'Organelle: {organelle}')
