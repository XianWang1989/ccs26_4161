
from Bio import Entrez
from Bio import SeqIO

# Assuming you have a list of accession numbers
accessions = ['ACCESSION_1', 'ACCESSION_2']  # Replace with your accession numbers
Entrez.email = "your_email@example.com"  # Always provide an email

for access in accessions:
    # Fetch the GenBank record with key annotations only
    handle = Entrez.efetch(db='nucleotide', id=access, rettype='gbwithparts', retmode='text')

    # Read the record
    record = SeqIO.read(handle, 'genbank')
    handle.close()  # Close the handle

    # Extract the taxonomy
    taxonomy = record.annotations.get('taxonomy', [])

    # Handle organelle information
    organelle = None
    for feature in record.features:
        if "organelle" in feature.qualifiers:
            organelle = feature.qualifiers["organelle"][0]
            break  # Exit once the organelle is found

    # Now you can perform your checks
    if 'Fungi' in taxonomy:
        # Increase your count
        fungi_count += 1  # Define `fungi_count` earlier in your code

    # Optionally store the relevant parts
    cache[access] = {
        'taxonomy': taxonomy,
        'organelle': organelle
    }
