
from Bio import SeqIO
from Bio import Entrez

# Always set your email when using Entrez
Entrez.email = "your_email@example.com"

def fetch_relevant_info(accessions):
    for acc in accessions:
        # Fetch GenBank file
        with Entrez.efetch(db='nucleotide', id=acc, rettype='gb', retmode='text') as gb_file:
            # Parse the GenBank record
            record = SeqIO.read(gb_file, 'genbank')

            # Extract organelle if available
            organelle = None
            for feature in record.features:
                if feature.type == 'source':
                    organelle = feature.qualifiers.get('organelle', [None])[0]
                    break

            # Extract taxonomy
            taxonomy = record.annotations.get('taxonomy', [])

            # Process your information
            print(f"Accession: {acc}")
            print(f"Organelle: {organelle}")
            print(f"Taxonomy: {taxonomy}")

# Example usage
accessions = ['NC_001416', 'NC_001422']  # Replace with your accession numbers
fetch_relevant_info(accessions)
