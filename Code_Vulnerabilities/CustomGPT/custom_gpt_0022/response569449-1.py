
from Bio import SeqIO
from Bio import Entrez

def fetch_features(accessions):
    Entrez.email = "your_email@example.com"  # Always set your email
    results = {}

    for access in accessions:
        try:
            handle = Entrez.efetch(db='nucleotide', id=access, rettype='gb', retmode='text')
            for record in SeqIO.parse(handle, 'genbank'):
                # Extract organelle feature
                organelle = None
                for feat in record.features:
                    if feat.type == 'organelle':
                        organelle = feat.qualifiers.get('organelle', [None])[0]

                # Extract taxonomy
                taxonomy = record.annotations.get('taxonomy', [])
                if len(taxonomy) > 1 and taxonomy[1] == 'Fungi':
                    # Store results
                    results[access] = {
                        'organelle': organelle,
                        'taxonomy': taxonomy
                    }
        except Exception as e:
            print(f"Error fetching {access}: {e}")
        finally:
            handle.close()

    return results

accession_numbers = ['ACCESSION1', 'ACCESSION2']  # Replace with actual accession numbers
features = fetch_features(accession_numbers)

print(features)
