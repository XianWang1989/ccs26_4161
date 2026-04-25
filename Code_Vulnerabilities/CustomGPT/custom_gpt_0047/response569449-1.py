
from Bio import Entrez
from Bio import SeqIO

def fetch_taxonomy_and_organelle(accession):
    Entrez.email = "your_email@example.com"  # Always provide your email
    # Fetch XML data from NCBI
    handle = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='xml')
    records = SeqIO.parse(handle, 'genbank')

    for record in records:
        # Access the taxonomy
        taxonomy = record.annotations.get('taxonomy', [])
        # Access the features to find organelle
        organelle = None
        for feature in record.features:
            if 'organelle' in feature.qualifiers:
                organelle = feature.qualifiers['organelle'][0]

        return taxonomy, organelle

# Example usage
accession_number = "Your_Accession_Number"
taxonomy, organelle = fetch_taxonomy_and_organelle(accession_number)

print("Taxonomy:", taxonomy)
print("Organelle:", organelle)
