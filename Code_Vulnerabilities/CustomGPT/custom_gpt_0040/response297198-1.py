
import pandas as pd

# Initialize an empty DataFrame to collect bad rows
bad_rows = []

# Read the CSV in chunks
for chunk in pd.read_csv('leads.csv', chunksize=1000):
    for col in chunk.columns:
        # Check for mixed types in each column
        mixed_types = chunk[col].apply(type).nunique() > 1
        if mixed_types:
            bad_rows.append(chunk[chunk[col].apply(type) != chunk[col].dtype.type])

# Combine all bad rows into a single DataFrame
if bad_rows:
    bad_data = pd.concat(bad_rows)
    print(bad_data)
else:
    print("No mixed type rows found.")
