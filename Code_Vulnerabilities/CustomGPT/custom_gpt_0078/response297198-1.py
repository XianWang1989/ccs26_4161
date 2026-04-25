
import pandas as pd

# Load the CSV in chunks
chunks = pd.read_csv('leads.csv', chunksize=1000)

# Check for inconsistent types in each chunk
for chunk in chunks:
    for col in ['Column11', 'Column12', 'Column13', 'Column14', 'Column17', 'Column19', 'Column20', 'Column21']:
        mixed_rows = chunk[~chunk[col].apply(lambda x: isinstance(x, (str, bool)))].index
        if not mixed_rows.empty:
            print(f"Inconsistent types found in column {col} at rows: {mixed_rows.tolist()}")
