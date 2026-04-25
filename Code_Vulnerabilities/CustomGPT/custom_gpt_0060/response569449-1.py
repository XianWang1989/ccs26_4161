
from Bio import Entrez
from Bio import SeqIO

# Set up Entrez email
Entrez.email = "your_email@example.com" 

def fetch_taxonomy_and_organelle(accession):
    # Fetch only metadata for the given accession
    try:
        handle = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text')
        record = SeqIO.read(handle, 'genbank')
        handle.close()  # Close the handle

        # Fetch the organelle information from features
        organelle_info = None
        for feature in record.features:
            if 'organelle' in feature.qualifiers:
                organelle_info = feature.qualifiers['organelle'][0]  # Get the first organelle info

        # Retrieve taxonomy information
        taxonomy_info = record.annotations.get('taxonomy', [])

        return taxonomy_info, organelle_info

    except Exception as e:
        print(f"Error fetching data for {accession}: {e}")
        return None, None

# Example usage
accession_number = "YOUR_ACCESSION_NUMBER"
taxonomy, organelle = fetch_taxonomy_and_organelle(accession_number)

if taxonomy:
    print("Taxonomy:", taxonomy)
if organelle:
    print("Organelle:", organelle)
