
import pandas as pd

# Define the columns that are causing issues
problematic_columns = [11, 12, 13, 14, 17, 19, 20, 21]

# Read the CSV in chunks
chunk_size = 1000  # Adjust the chunk size as needed
for chunk in pd.read_csv('leads.csv', chunksize=chunk_size):
    # Check the data types of the problematic columns
    for col in problematic_columns:
        # Check if the column has mixed types
        if chunk.iloc[:, col].apply(type).nunique() > 1:
            print(f"Mixed types found in chunk for column {col}:")
            print(chunk.iloc[:, col].unique())
