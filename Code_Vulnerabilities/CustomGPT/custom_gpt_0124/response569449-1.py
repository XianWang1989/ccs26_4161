
from Bio import SeqIO
from Bio import Entrez

# Function to fetch only the required fields from GenBank
def fetch_genbank_parts(accession):
    Entrez.email = "your_email@example.com"  # Always set your email
    handle = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text')

    # Instead of reading the entire record, we can parse it as text
    for record in SeqIO.parse(handle, 'genbank'):
        # Extract taxonomy
        taxonomy = record.annotations.get('taxonomy', [])
        organelle = None

        # Extract organelle feature if exists
        for feature in record.features:
            if 'organelle' in feature.qualifiers:
                organelle = feature.qualifiers['organelle'][0]
                break

        # Return only the extracted information
        return {
            'taxonomy': taxonomy,
            'organelle': organelle
        }

# Example usage
accession = "YOUR_ACCESSION_NUMBER"
result = fetch_genbank_parts(accession)
print("Taxonomy:", result['taxonomy'])
print("Organelle:", result['organelle'])
