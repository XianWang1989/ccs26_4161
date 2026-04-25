
import pandas as pd

# Specify the chunksize
chunk_size = 1000
problematic_rows = []

# Iterate through the CSV in chunks
for chunk in pd.read_csv('leads.csv', chunksize=chunk_size):
    for index, row in chunk.iterrows():
        # Check specific columns for inconsistent types
        if not row[11] in ['TRUE', 'FALSE'] or not isinstance(row[11], str):
            problematic_rows.append(index)

print("Problematic row indices:", problematic_rows)
