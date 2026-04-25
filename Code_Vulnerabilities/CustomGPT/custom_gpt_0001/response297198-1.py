
import pandas as pd

# Define the columns to check for dtype consistency
columns_to_check = [11, 12, 13, 14, 17, 19, 20, 21]  # Adjust based on zero-indexing

# Read the CSV in chunks and check for dtype discrepancies
chunk_size = 1000
for chunk in pd.read_csv('leads.csv', chunksize=chunk_size):
    for col in columns_to_check:
        # Collect unique data types for the column
        unique_types = set(chunk.iloc[:, col].map(type))
        if len(unique_types) > 1:
            print(f"Column {col} has mixed types: {unique_types}")
            # Optionally, print the rows with inconsistent types
            print(chunk[chunk.iloc[:, col].apply(lambda x: type(x) not in unique_types)])
