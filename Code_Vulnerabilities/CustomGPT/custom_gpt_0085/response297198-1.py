
import pandas as pd

# Reading the CSV in chunks
chunk_size = 1000  # Adjust the chunk size as needed
problematic_rows = []

for chunk in pd.read_csv('leads.csv', chunksize=chunk_size):
    for col in [11, 12, 13, 14, 17, 19, 20, 21]:  # Columns with issues
        if chunk[col].dtype == 'object':
            problematic_rows.extend(chunk[chunk[col].isna() | (chunk[col].astype(str).str.contains(r'[^A-Za-z0-9]'))].index.tolist())

# Remove duplicates
problematic_rows = set(problematic_rows)
print(f"Problematic row indices: {sorted(problematic_rows)}")
