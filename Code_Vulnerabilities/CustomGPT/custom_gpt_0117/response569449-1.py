
from Bio import SeqIO
from Bio import Entrez

Entrez.email = "your_email@example.com"  # Always include your email

def fetch_taxonomy_and_organelle(accession):
    # Fetch the record
    gb_record = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text')
    record = SeqIO.read(gb_record, 'genbank')

    # Extract the organelle information
    organelle = None
    for feature in record.features:
        if feature.type == 'source':
            if 'organelle' in feature.qualifiers:
                organelle = feature.qualifiers['organelle'][0]

    # Extract taxonomy information
    taxonomy = record.annotations.get('taxonomy', [])

    return organelle, taxonomy

# Example usage
accession_number = "YOUR_ACCESSION_NUM"
organelle, taxonomy = fetch_taxonomy_and_organelle(accession_number)

print("Organelle:", organelle)
print("Taxonomy:", taxonomy)
