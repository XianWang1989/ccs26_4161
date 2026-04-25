
from Bio import Entrez
from Bio import SeqIO

# Function to fetch only the required features from GenBank
def fetch_genbank_data(accession):
    try:
        # Fetch the GenBank data for the given accession
        with Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text') as handle:
            # Parse the file line by line
            for record in SeqIO.parse(handle, 'genbank'):
                # Check and get the taxonomy
                taxonomy = record.annotations.get('taxonomy', [])
                if len(taxonomy) > 1 and taxonomy[1] == 'Fungi':
                    # Handle your fungi condition here
                    print(f"{accession} is in Fungi")

                # Check for organelle feature
                for feature in record.features:
                    if feature.type == 'organelle':
                        organelle_info = feature.qualifiers.get('organelle', [])
                        if organelle_info:
                            print(f"Organelle found in {accession}: {organelle_info}")

                # Return early if you just need one accession
                return  # Remove this if you want to fetch multiple records
    except Exception as e:
        print(f"Error occurred for {accession}: {e}")

# Example usage
Entrez.email = "your_email@example.com"  # Always provide an email
accessions = ['ACCESSION1', 'ACCESSION2']  # Replace with your list of accession numbers

for acc in accessions:
    fetch_genbank_data(acc)
