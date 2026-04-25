
import pandas as pd

# Read the CSV in chunks
chunk_size = 1000
for chunk in pd.read_csv('leads.csv', chunksize=chunk_size):
    # Check data types of the current chunk
    print(chunk.dtypes)

    # Check for rows that may not fit expected types (e.g., bool should only be True/False)
    if chunk['Column_K'].apply(lambda x: x not in [True, False, 'TRUE', 'FALSE', '']).any():
        print("Mismatched values found in Column K:")
        print(chunk[~chunk['Column_K'].isin([True, False, 'TRUE', 'FALSE', ''])])
