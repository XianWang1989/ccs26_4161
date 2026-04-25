
from Bio import SeqIO
from Bio import Entrez

# Fetch function that retrieves specific features
def fetch_taxonomy_and_organelle(accession):
    Entrez.email = "your_email@example.com"  # Always provide your email
    try:
        with Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text') as gb_file:
            for record in SeqIO.parse(gb_file, 'genbank'):
                # Extract taxonomy
                taxonomy = record.annotations.get('taxonomy', [])

                # Check for organelle features
                organelles = [feature for feature in record.features if feature.type == 'organelle']

                # Print the extracted information
                if taxonomy:
                    print(f"Taxonomy for {accession}: {taxonomy}")
                else:
                    print(f"No taxonomy found for {accession}")

                if organelles:
                    for organelle in organelles:
                        print(f"Organelle for {accession}: {organelle.qualifiers.get('organelle', ['N/A'])[0]}")
                else:
                    print(f"No organelle feature found for {accession}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Sample usage
accession_number = "YOUR_ACCESSION_NUMBER"
fetch_taxonomy_and_organelle(accession_number)
