
from Bio import Entrez

# Set your email for Entrez
Entrez.email = "your_email@example.com"

def fetch_taxonomy_and_organelle(accession):
    # Fetch record summary (which contains taxonomy)
    summary_handle = Entrez.esummary(db='nucleotide', id=accession)
    summary_record = Entrez.read(summary_handle)
    taxonomy = summary_record[0]['Taxonomy']

    # Now fetch the GenBank file to check for organelle
    gb_handle = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text')
    gb_record = SeqIO.read(gb_handle, 'genbank')

    # Search for organelle in features
    organelle = None
    for feature in gb_record.features:
        if 'organelle' in feature.qualifiers:
            organelle = feature.qualifiers['organelle'][0]
            break

    return taxonomy, organelle

# Example usage
accession_number = "YOUR_ACCESSION_NUMBER"
taxonomy, organelle = fetch_taxonomy_and_organelle(accession_number)
print("Taxonomy:", taxonomy)
print("Organelle:", organelle)
