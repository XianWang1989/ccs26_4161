
import pandas as pd

# First, let's read the CSV in chunks to find problematic rows
chunk_size = 1000
problematic_rows = []

for chunk in pd.read_csv('leads.csv', chunksize=chunk_size):
    # Check the datatypes of the columns
    for col in ['column_11', 'column_12', 'column_13']:  # replace with actual column names
        if chunk[col].dtype == 'object':
            mixed_type_rows = chunk[chunk[col].apply(lambda x: isinstance(x, str) and x not in ['TRUE', 'FALSE'])]
            problematic_rows.append(mixed_type_rows)

# Concatenate all problematic rows if any
if problematic_rows:
    problematic_df = pd.concat(problematic_rows)
    print("Problematic Rows:")
    print(problematic_df)

# Now reading the CSV with specified data types
data = pd.read_csv('leads.csv', dtype={
    'column_11': 'bool',  # specify appropriate dtype
    'column_12': 'str',   # adjust as necessary
    'column_13': 'str',   # adjust as necessary
}, low_memory=False)

print(data.head())
