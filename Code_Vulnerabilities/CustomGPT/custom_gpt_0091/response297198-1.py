
import pandas as pd

# Read the CSV in chunks
chunk_size = 1000  # Adjust based on your dataset size
problematic_rows = []

# Iterate through chunks
for chunk in pd.read_csv('leads.csv', chunksize=chunk_size):
    # Check for mixed types in specified columns
    for col in [11, 12, 13, 14, 17, 19, 20, 21]:  # Adjust columns as needed
        mixed_types = chunk[col].apply(type).nunique()
        if mixed_types > 1:
            problematic_rows.extend(chunk.index[chunk[col].apply(type).ne(chunk[col].dtype)])

# Check for unique problematic indices
unique_problematic_rows = set(problematic_rows)
print(f"Problematic rows: {unique_problematic_rows}")
