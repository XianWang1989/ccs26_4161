
from Bio import Entrez
import xml.etree.ElementTree as ET

# Set your email for Entrez
Entrez.email = "your_email@example.com"

def fetch_taxonomy_and_organelle(accession):
    # Fetch the GenBank record in XML format
    handle = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='xml')
    record = ET.parse(handle).getroot()

    # Initialize variables
    taxonomy = None
    organelle = None

    # Parse the XML to extract taxonomy and organelle information
    for gb in record.findall("GBSeq"):
        # Get taxonomy
        taxonomy = gb.find("GBSeq_taxonomy").text
        # Get features
        for feature in gb.findall("GBSeq_feature-table/GBFeature"):
            for qualifier in feature.findall("GBQualifier"):
                if qualifier.find("GBQualifier_name").text == "organelle":
                    organelle = qualifier.find("GBQualifier_value").text

    return taxonomy, organelle

# Example usage
accession_number = "YOUR_ACCESSION_NUMBER"
taxonomy, organelle = fetch_taxonomy_and_organelle(accession_number)

print(f"Taxonomy: {taxonomy}")
print(f"Organelle: {organelle}")
