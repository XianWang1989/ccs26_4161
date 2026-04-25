
from Bio import SeqIO
from Bio import Entrez

Entrez.email = "your_email@example.com"  # Always include your email

def fetch_genbank_info(accession):
    # Fetch the GenBank record
    gb_handle = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text')

    # Read the record
    record = SeqIO.read(gb_handle, 'genbank')
    gb_handle.close()  # Close the handle to free resources

    # Extract taxonomy information
    taxonomy = record.annotations.get('taxonomy', [])
    organelle = None

    # Check for organelle information in features
    for feature in record.features:
        if 'organelle' in feature.qualifiers:
            organelle = feature.qualifiers['organelle'][0]

    return taxonomy, organelle

# Example usage
accession_number = "YOUR_ACCESSION_NUMBER"
taxonomy_info, organelle_info = fetch_genbank_info(accession_number)

print("Taxonomy:", taxonomy_info)
print("Organelle:", organelle_info)
