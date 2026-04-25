
import pandas as pd

# Read the CSV file in chunks and check each chunk for data types
chunk_size = 1000  # Adjust this based on your needs
problematic_rows = []

for chunk in pd.read_csv('leads.csv', chunksize=chunk_size):
    for column in chunk.columns:
        if chunk[column].dtype == 'object':  # Check for object types
            mixed_type_rows = chunk[chunk[column].apply(lambda x: isinstance(x, str) and not x.isalnum())]
            if not mixed_type_rows.empty:
                problematic_rows.append((column, mixed_type_rows))

# Display problematic rows
for column, rows in problematic_rows:
    print(f"Column: {column}, Problematic Rows: {rows}")
