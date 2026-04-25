
from Bio import Entrez

# Function to fetch only necessary parts from a GenBank file
def fetch_genbank_info(accession):
    Entrez.email = "your_email@example.com"  # Always include your email
    # Fetch the GenBank record
    handle = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text')

    # Read the entire file as a string
    gb_data = handle.read()
    handle.close()

    # Extract taxonomy (simple string parsing)
    taxonomy_start = gb_data.find("taxonomy") + len("taxonomy") + 1
    taxonomy_end = gb_data.find("\n", taxonomy_start)
    taxonomy = gb_data[taxonomy_start:taxonomy_end].strip().split("; ")

    # Extract organelle (assuming it's in the first feature)
    features_start = gb_data.find("FEATURES") + len("FEATURES") + 1
    features = gb_data[features_start:].strip().split("ORIGIN")[0]

    organelle = None
    if "organelle" in features:
        organelle_line = features[features.find("organelle"):].splitlines()[0]
        organelle = organelle_line.split('=')[1].strip().strip('"')

    return taxonomy, organelle

# Example usage
accession_number = "YOUR_ACCESSION_NUMBER"
taxonomy, organelle = fetch_genbank_info(accession_number)
print("Taxonomy:", taxonomy)
print("Organelle:", organelle)
