
import pandas as pd

# Define a function to check for mixed types
def check_column_types(chunk):
    for column in chunk.columns:
        unique_types = chunk[column].apply(type).unique()
        if len(unique_types) > 1:
            print(f"Column {column} has mixed types: {unique_types}")

# Read the CSV in chunks
chunk_size = 1000
for chunk in pd.read_csv('leads.csv', chunksize=chunk_size):
    check_column_types(chunk)
