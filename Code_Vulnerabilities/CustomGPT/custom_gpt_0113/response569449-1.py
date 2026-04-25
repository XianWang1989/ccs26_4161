
from Bio import Entrez
from Bio import SeqIO

# Replace with your actual accession number
access1 = "YOUR_ACCESSION_NUMBER"

# Set email for Entrez
Entrez.email = "your_email@example.com"

# Fetch the summary using efetch
handle = Entrez.efetch(db='nucleotide', id=access1, rettype='gb', retmode='text')
genbank_record = SeqIO.read(handle, 'genbank')
handle.close()

# Extracting taxonomy
taxonomy = genbank_record.annotations.get('taxonomy', [])
if 'Fungi' in taxonomy:
    # Example action when taxonomy matches
    print(f"{access1} is classified as Fungi.")

# Checking for organelle feature
for feature in genbank_record.features:
    if 'organelle' in feature.qualifiers:
        organelle = feature.qualifiers['organelle'][0]
        print(f"Organelle: {organelle}")
        break  # Exit after finding the organelle

# Optionally cache the record
cache = {}
cache[access1] = genbank_record
