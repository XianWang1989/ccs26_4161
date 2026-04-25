
from Bio import Entrez
from xml.etree import ElementTree

# Function to fetch and parse taxonomy and organelle
def fetch_taxonomy_organelle(access1):
    Entrez.email = "your_email@example.com"  # Always provide your email
    # Fetch XML data
    with Entrez.efetch(db='nucleotide', id=access1, rettype='gb', retmode='xml') as handle:
        tree = ElementTree.parse(handle)
        root = tree.getroot()

        # Extract taxonomy
        taxonomy_element = root.find(".//taxonomy")
        taxonomy = [taxon.text for taxon in taxonomy_element] if taxonomy_element is not None else []

        # Extract organelle
        organelle = None
        features = root.findall(".//feature")
        for feature in features:
            if feature.get('name') == 'organelle':
                organelle = feature.find('value').text if feature.find('value') is not None else None

        return taxonomy, organelle

# Example usage
accession_number = 'YOUR_ACCESSION_NUMBER'
taxonomy, organelle = fetch_taxonomy_organelle(accession_number)

print("Taxonomy:", taxonomy)
print("Organelle:", organelle)
