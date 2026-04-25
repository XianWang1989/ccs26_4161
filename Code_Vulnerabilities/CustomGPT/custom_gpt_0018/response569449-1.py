
from Bio import SeqIO
from Bio import Entrez

# Set your email for NCBI Entrez
Entrez.email = "your_email@example.com"

def fetch_and_process(accession):
    try:
        # Fetch the record
        gb_record = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text')
        rec = SeqIO.read(gb_record, 'genbank')

        # Check for organelle feature
        organelle = None
        for feature in rec.features:
            if feature.type == 'source' and 'organelle' in feature.qualifiers:
                organelle = feature.qualifiers['organelle'][0]
                break

        # Check for taxonomy
        taxonomy = rec.annotations.get('taxonomy', [])
        if len(taxonomy) > 1 and taxonomy[1] == 'Fungi':
            # handle fungi case
            print(f"{accession} is of Fungi")

        return organelle

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
accession_number = 'YOUR_ACCESSION_NUMBER'
organelle_info = fetch_and_process(accession_number)
if organelle_info:
    print(f"Organelle info for {accession_number}: {organelle_info}")
