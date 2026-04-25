
import pandas as pd

# Read the CSV in chunks
for chunk in pd.read_csv('leads.csv', chunksize=1000):
    # Check the data types of each column in the chunk
    print(chunk.dtypes)
    # Identify rows with mixed types in specified columns
    mixed_types = chunk[['Column11', 'Column12', 'Column13']].applymap(type)
    print(mixed_types[mixed_types.nunique(axis=1) > 1])  # Shows rows with mixed types
