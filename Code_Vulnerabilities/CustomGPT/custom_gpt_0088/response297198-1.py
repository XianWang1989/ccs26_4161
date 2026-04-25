
import pandas as pd

# Read a chunk of the CSV file
chunk_size = 1000  # Adjust this size as needed
mixed_rows = []

for chunk in pd.read_csv('leads.csv', chunksize=chunk_size):
    # Check for mixed types in the specific columns
    for col in ['column_11', 'column_12', 'column_13', 'column_14', 'column_17', 'column_19', 'column_20', 'column_21']:
        if chunk[col].dtype == 'object':  # This indicates potential mixed types
            mixed_rows.extend(chunk[chunk[col].apply(lambda x: isinstance(x, str) and x.strip().lower() not in ['true', 'false', ''])].index.tolist())

# Remove duplicates
mixed_rows = set(mixed_rows)
print(f"Rows with mixed types: {mixed_rows}")
