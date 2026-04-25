
from Bio import Entrez

# Function to get taxonomy and organelle information
def get_taxonomy_and_organelle(accession):
    Entrez.email = "your_email@example.com"  # Always provide your email
    # Fetch metadata only 
    handle = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text')

    # Read only the relevant features from the GenBank record
    record = SeqIO.read(handle, 'genbank')
    handle.close()

    tax_info = record.annotations.get('taxonomy', [])
    organelle_info = ""

    for feature in record.features:
        if feature.type == 'source':
            organelle_info = feature.qualifiers.get('organelle', [''])[0]
            break

    return tax_info, organelle_info

# Example usage
accession = "YOUR_ACCESSION_NUMBER"  # Replace with your accession number
taxonomy, organelle = get_taxonomy_and_organelle(accession)

# Check results
print(f"Taxonomy: {taxonomy}")
print(f"Organelle: {organelle}")
