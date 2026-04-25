
import pandas as pd

# Define the columns to check
columns_to_check = [11, 12, 13, 14, 17, 19, 20, 21]  # Adjust for zero-indexing

# Read the CSV in chunks and check for dtypes
chunk_size = 1000
inconsistent_rows = []

for chunk in pd.read_csv('leads.csv', chunksize=chunk_size):
    for col in columns_to_check:
        if chunk.iloc[:, col].apply(type).nunique() > 1:
            inconsistent_rows.append(chunk.iloc[:, col][chunk.iloc[:, col].apply(type).ne(chunk.iloc[:, col].iloc[0].dtype)].index.tolist())

# Flatten the list and remove duplicates
inconsistent_rows = set(sum(inconsistent_rows, []))
print(f"Inconsistent rows: {inconsistent_rows}")
