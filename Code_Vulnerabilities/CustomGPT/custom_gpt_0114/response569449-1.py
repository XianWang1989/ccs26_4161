
from Bio import Entrez

Entrez.email = "your_email@example.com"  # Always include your email

def fetch_taxonomy_and_organelle(accession):
    # Fetch the GenBank record
    handle = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text')

    # Search through the handle line by line
    tax_info = None
    organelle_info = None

    for line in handle:
        # Check for taxonomy
        if line.startswith("  ORGANISM"):
            tax_info = line.strip().split(" ")[1:]  # Extract taxonomy info
        # Check for organelle feature
        if "organelle" in line:
            organelle_info = line.strip()

    handle.close()
    return tax_info, organelle_info


# Example usage
accession_number = "YOUR_ACCESSION_NUMBER"
taxonomy, organelle = fetch_taxonomy_and_organelle(accession_number)

if taxonomy:
    print("Taxonomy:", ' '.join(taxonomy))
if organelle:
    print("Organelle:", organelle)
