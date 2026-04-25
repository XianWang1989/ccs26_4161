
import pandas as pd

# Define the CSV file path
csv_file_path = 'leads.csv'

# Load the CSV in chunks
chunk_size = 1000  # Adjust this to the size that makes sense for your data
chunks = pd.read_csv(csv_file_path, chunksize=chunk_size)

# Track issues
for chunk in chunks:
    problematic_rows = chunk[[11, 12, 13, 14, 17, 19, 20, 21]].applymap(type)
    print(problematic_rows.apply(lambda col: col.unique()))
