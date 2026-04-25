
from Bio import Entrez

# Set your email here (required by NCBI)
Entrez.email = 'your_email@example.com'

def fetch_taxonomy_and_organelle(accession):
    try:
        # Fetch the GenBank record
        handle = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text')
        data = handle.read()
        handle.close()

        # Split the data into lines
        lines = data.split('\n')

        # Initialize variables
        taxonomy = None
        organelle = None

        for line in lines:
            # Check for the taxonomy line
            if line.startswith('OC'):
                taxonomy = line[5:].strip()  # Extract and clean the taxonomy line
            # Check for organelle feature in lines starting with '     organelle'
            if line.startswith('     organelle'):
                organelle = line[14:].strip()  # Extract and clean the organelle feature line

        return taxonomy, organelle

    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None

# Example usage
accession_number = 'YOUR_ACCESSION_NUMBER'
taxonomy, organelle = fetch_taxonomy_and_organelle(accession_number)

if taxonomy and organelle:
    print(f"Taxonomy: {taxonomy}")
    print(f"Organelle: {organelle}")
else:
    print("Could not retrieve the required information.")
