
from Bio import Entrez, SeqIO

# Function to retrieve taxonomic data without fetching the full GenBank record
def get_taxonomy(acc_number):
    Entrez.email = "your_email@example.com"  # Always include your email
    handle = Entrez.esummary(db="nucleotide", id=acc_number)
    record_summary = Entrez.read(handle)
    handle.close()

    # Return the taxonomy if available, else return None
    return record_summary[0]["Taxonomy"] if "Taxonomy" in record_summary[0] else None

# Function to fetch only organelle information
def get_organelle(acc_number):
    Entrez.email = "your_email@example.com"  # Always include your email
    handle = Entrez.efetch(db="nucleotide", id=acc_number, rettype="gb", retmode="text")
    rec = SeqIO.read(handle, "genbank")
    handle.close()

    # Retrieve the organelle if available
    for feature in rec.features:
        if 'organelle' in feature.qualifiers:
            return feature.qualifiers['organelle']
    return None

# Example usage
access1 = "YOUR_ACCESSION_NUMBER"  # replace with the actual accession number
taxonomy = get_taxonomy(access1)

if taxonomy and 'Fungi' in taxonomy:
    organelle_info = get_organelle(access1)  # Fetch organelle details only if taxonomy matches
    print(f"Organelle Information for {access1}: {organelle_info}")
else:
    print(f"Taxonomy for {access1} is not 'Fungi'.")
