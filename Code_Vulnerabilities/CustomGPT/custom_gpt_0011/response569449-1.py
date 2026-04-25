
from Bio import Entrez
import xml.etree.ElementTree as ET

def fetch_taxonomy_and_organelle(accession):
    Entrez.email = "your-email@example.com"  # Always provide your email
    try:
        # Fetch the XML data
        response = Entrez.efetch(db='nucleotide', id=accession, rettype='xml', retmode='text')
        xml_data = ET.parse(response)

        # Extract relevant data
        for record in xml_data.findall('.//DNASet'):
            # For taxonomy
            taxonomy = record.find('.//Taxonomy').text if record.find('.//Taxonomy') is not None else None
            print(f'Taxonomy for {accession}: {taxonomy}')

            # For organelle (if available in the record)
            organelle = record.find('.//organelle').text if record.find('.//organelle') is not None else None
            print(f'Organelle for {accession}: {organelle}')

    except Exception as e:
        print(f'Error occurred: {e}')

# Example accession numbers
accession_numbers = ["accession1", "accession2"]  # replace with actual accession numbers

for acc in accession_numbers:
    fetch_taxonomy_and_organelle(acc)
