
import pandas as pd

# Create an empty list to store problematic rows
problematic_rows = []

# Read the CSV in chunks
chunk_size = 1000  # Adjust chunk size if needed
for chunk in pd.read_csv('leads.csv', chunksize=chunk_size):
    for column in chunk.columns:
        # Check for mixed types in the column
        if chunk[column].apply(type).nunique() > 1:
            # Append problematic rows to the list
            problematic_rows.append(chunk[chunk[column].apply(type).ne(type(chunk[column].iloc[0]))])

# Concatenate all problematic rows into a single DataFrame
problematic_data = pd.concat(problematic_rows)
print(problematic_data)
