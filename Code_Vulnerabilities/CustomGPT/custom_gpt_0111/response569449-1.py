
from Bio import Entrez
from Bio import SeqIO

# Function to fetch minimal metadata
def fetch_metadata(accession):
    Entrez.email = "your_email@example.com"  # Always set your email
    summary = Entrez.esummary(db='nucleotide', id=accession)
    record = Entrez.read(summary)

    # Extracting taxonomy
    taxonomy = record[0]['TaxName']
    return taxonomy

# Function to fetch only necessary features
def fetch_organelle(accession):
    gb_acc = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text')
    rec = SeqIO.read(gb_acc, 'genbank')

    # Extracting organelle
    organelle = None
    for feat in rec.features:
        if 'organelle' in feat.qualifiers:
            organelle = feat.qualifiers['organelle'][0]
            break
    return organelle

# Main logic
accession_number = "YOUR_ACCESSION"  # Replace with your actual accession number
taxonomy = fetch_metadata(accession_number)

if taxonomy == 'Fungi':
    organelle = fetch_organelle(accession_number)
    print(f"Organelle: {organelle}")

# Example of handling multiple accessions
accession_numbers = ["ACC1", "ACC2"]  # List of accession numbers
for acc in accession_numbers:
    taxonomy = fetch_metadata(acc)
    if taxonomy == 'Fungi':
        organelle = fetch_organelle(acc)
        print(f"Accession: {acc}, Organelle: {organelle}")
