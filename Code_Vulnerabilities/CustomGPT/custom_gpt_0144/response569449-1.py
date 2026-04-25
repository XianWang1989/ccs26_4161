from Bio import Entrez
from Bio import SeqIO

# Function to fetch GenBank record and extract only required metadata (taxonomy, organelle)
def fetch_genbank_metadata(accession):
    # Fetch metadata (without downloading full GenBank record)
    handle = Entrez.efetch(db="nucleotide", id=accession, rettype="gb", retmode="text")
    
    # Parse the GenBank record and get annotations
    record = SeqIO.read(handle, "genbank")
    
    # Extract taxonomy
    taxonomy = record.annotations.get("taxonomy", [])
    
    # Extract organelle from features
    organelle = None
    for feature in record.features:
        if feature.type == "source" and 'organism' in feature.qualifiers:
            organelle = feature.qualifiers.get('organism', [])
            break
    
    # Return the relevant data (taxonomy and organelle)
    return taxonomy, organelle

# Example usage
accession = "NC_000913"  # Replace with your accession number
taxonomy, organelle = fetch_genbank_metadata(accession)

# Example print out
print("Taxonomy:", taxonomy)
print("Organelle:", organelle)
