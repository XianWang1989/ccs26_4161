
from Bio import Entrez

# Function to fetch required information from GenBank
def fetch_taxonomy_and_organelle(accession):
    Entrez.email = "your_email@example.com"  # Always include your email
    handle = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text')

    # Read the GenBank record
    record = SeqIO.read(handle, 'genbank')

    # Extract taxonomy
    taxonomy = record.annotations.get('taxonomy', [])
    if taxonomy:
        target_taxonomy = taxonomy[1] if len(taxonomy) > 1 else None

    # Extract organelle information
    organelle = None
    for feature in record.features:
        if 'organelle' in feature.qualifiers:
            organelle = feature.qualifiers['organelle'][0]
            break

    handle.close()
    return target_taxonomy, organelle

# Example usage
accession_number = 'YOUR_ACCESSION_NUMBER'  # Replace with actual accession
taxonomy, organelle = fetch_taxonomy_and_organelle(accession_number)

if taxonomy == 'Fungi':
    fungi_count += 1

print("Taxonomy:", taxonomy)
print("Organelle:", organelle)
