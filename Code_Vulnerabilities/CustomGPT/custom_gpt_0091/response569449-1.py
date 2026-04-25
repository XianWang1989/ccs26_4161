
from Bio import Entrez
from xml.etree import ElementTree as ET

# Set your email
Entrez.email = "your_email@example.com"

def fetch_taxonomy_and_organelle(accession):
    # Fetch data in XML format to minimize data transfer
    with Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='xml') as handle:
        data = handle.read()
        xml_tree = ET.fromstring(data)

    # Extract taxonomy
    taxonomy = None
    organelle = None

    # Parse the XML data
    for elem in xml_tree.iter('GBSeq'):
        for tax in elem.findall('GBSeq_taxonomy'):
            taxonomy = tax.text
        for feature in elem.findall('GBFeature'):
            for qualifier in feature.findall('GBQualifier'):
                if qualifier.find('GBQualifier_name').text == 'organelle':
                    organelle = qualifier.find('GBQualifier_value').text

    return taxonomy, organelle

# Example usage
accession = "your_accession_number_here"
taxonomy, organelle = fetch_taxonomy_and_organelle(accession)

if taxonomy:
    print(f"Taxonomy: {taxonomy}")
if organelle:
    print(f"Organelle: {organelle}")
