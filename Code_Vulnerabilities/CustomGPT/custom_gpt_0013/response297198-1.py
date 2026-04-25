
import pandas as pd

# Read the CSV in chunks to identify problematic rows
chunk_size = 1000  # Adjust as needed
for chunk in pd.read_csv('leads.csv', chunksize=chunk_size):
    print(chunk.dtypes)  # Print dtypes for each chunk
    # Optionally check for unique values in suspect columns
    print(chunk[['ColumnK', 'ColumnX']].unique())  # Replace with actual column names
