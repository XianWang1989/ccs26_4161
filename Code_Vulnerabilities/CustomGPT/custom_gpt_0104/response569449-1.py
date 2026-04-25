
from Bio import Entrez

# Your email and accesion number list
Entrez.email = "your_email@example.com"
accession_numbers = ['ACCESSION_1', 'ACCESSION_2']

# Initialize counters for fungi
fungi_count = 0

for access in accession_numbers:
    # First, fetch a summary of the GenBank record
    summary_handle = Entrez.esummary(db='nucleotide', id=access, retmode='xml')
    summary_records = Entrez.read(summary_handle)

    # Get taxonomy information from the summary
    tax_id = summary_records[0]['TaxId']

    # Now, you might use the taxonomy ID to get taxonomy info
    taxonomy_handle = Entrez.efetch(db='taxonomy', id=tax_id, retmode='xml')
    taxonomy_records = Entrez.read(taxonomy_handle)

    # Extract the necessary taxonomy information
    if taxonomy_records and 'Lineage' in taxonomy_records[0]:
        # Check if it's Fungi
        if 'Fungi' in taxonomy_records[0]['Lineage']:
            fungi_count += 1

    # Optionally, if you need organelle information, fetch the record
    gb_handle = Entrez.efetch(db='nucleotide', id=access, rettype='gb', retmode='text')
    rec = SeqIO.read(gb_handle, 'genbank')

    # Check for organelle as needed
    for feat in rec.features:
        if feat.type == 'source' and 'organelle' in feat.qualifiers.keys():
            organelle_info = feat.qualifiers['organelle'][0]
            print(f"Accession: {access}, Organelle: {organelle_info}")

# Finally, print the Fungi count
print(f"Number of Fungi records: {fungi_count}")
