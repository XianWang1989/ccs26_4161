
from Bio import Entrez
import xml.etree.ElementTree as ET

# Set your email for Entrez
Entrez.email = "your_email@example.com"

def fetch_taxonomy_and_organelle(accession):
    # Fetch the summary which is smaller than full GenBank records
    handle = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='xml')
    records = ET.parse(handle).getroot()

    taxonomy = None
    organelle = None

    for record in records:
        # Access the taxonomy
        taxonomy = record.find("Taxon").text if record.find("Taxon") is not None else None

        # Access features and qualifiers for organelle
        features = record.find("Features")
        if features is not None:
            for feature in features.findall("Feature"):
                if feature.get("qualifiers") and 'organelle' in feature.get("qualifiers"):
                    organelle = feature.get("qualifiers")['organelle'][0]
                    break

    return taxonomy, organelle

# Example usage
access1 = "YOUR_ACCESSION_NUMBER"  # Replace with your accession number
taxonomy, organelle = fetch_taxonomy_and_organelle(access1)

if taxonomy:
    print("Taxonomy:", taxonomy)
if organelle:
    print("Organelle:", organelle)
