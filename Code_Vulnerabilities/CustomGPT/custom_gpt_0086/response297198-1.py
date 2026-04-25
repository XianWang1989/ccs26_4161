
import pandas as pd

# Initialize an empty list to store problematic rows
problematic_rows = []

# Read CSV in chunks
chunk_size = 1000  # Adjust chunk size if needed
for chunk in pd.read_csv('leads.csv', chunksize=chunk_size):
    for col in chunk.columns:
        # Check for mixed types in each column
        if chunk[col].apply(type).nunique() > 1:
            problematic_rows.append(chunk[chunk[col].apply(type) != chunk[col].dtype.type])

# Convert list to DataFrame for easier inspection
problematic_rows_df = pd.concat(problematic_rows)

print(problematic_rows_df)
