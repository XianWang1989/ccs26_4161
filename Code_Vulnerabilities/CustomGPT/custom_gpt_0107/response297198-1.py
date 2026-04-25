
import pandas as pd

# Define the file path
file_path = 'leads.csv'

# Read the CSV in chunks
chunk_size = 1000
mixed_rows = []

for chunk in pd.read_csv(file_path, chunksize=chunk_size):
    for col in [11, 12, 13, 14, 17, 19, 20, 21]:  # Columns with potential issues
        mixed = chunk[col].apply(type).nunique()  # Count unique types in the column
        if mixed > 1:
            mixed_rows.extend(chunk[chunk[col].apply(type) != chunk[col].iloc[0]].index.tolist())

# Remove duplicates and print indices of problematic rows
mixed_rows = list(set(mixed_rows))
print("Problematic row indices:", mixed_rows)
