
import pandas as pd

# Specify the path to your CSV file
file_path = 'leads.csv'

# Use a chunk size to read the file in parts
chunk_size = 1000
problematic_rows = []

for chunk in pd.read_csv(file_path, chunksize=chunk_size):
    for col in chunk.columns:
        # Check the dtypes of each column
        mixed_types = chunk[col].apply(type).nunique() > 1
        if mixed_types:
            problematic_rows += list(chunk.index)

# Display unique problematic row indices
unique_problematic_rows = set(problematic_rows)
print(f'Problematic row indices: {unique_problematic_rows}')
