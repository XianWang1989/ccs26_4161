
from Bio import SeqIO
from Bio import Entrez

# Initialize the Entrez email
Entrez.email = "your_email@example.com"  # Replace with your email

access1 = "your_accession_number_here"
fungi_count = 0

# Fetch GenBank record
gb_file = Entrez.efetch(db='nucleotide', id=access1, rettype='gb', retmode='text')

# Use SeqIO to parse and minimize the data you care about
record = SeqIO.read(gb_file, 'genbank')

# Check for organelle in features
for feat in record.features:
    if feat.type == "source":  # The source feature typically contains taxonomy
        if 'organelle' in feat.qualifiers:
            organelle = feat.qualifiers['organelle'][0]
            print(f"Organelle: {organelle}")

        # Check taxonomy
        if 'taxonomy' in record.annotations:
            taxonomy = record.annotations['taxonomy']
            if taxonomy and taxonomy[1] == 'Fungi':
                fungi_count += 1
                print(f"Taxonomy includes Fungi.")

print(f"Total number of fungi: {fungi_count}")
