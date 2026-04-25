
import pandas as pd

# Step 1: Initial read with all columns as strings to spot inconsistencies
df = pd.read_csv('leads.csv', dtype=str)

# Step 2: Check specific columns for unique types
inconsistent_rows = {}
columns_to_check = ['Column11', 'Column12', 'Column13', 'Column14', 'Column17', 'Column19', 'Column20', 'Column21']

for column in columns_to_check:
    # Identify rows where types are inconsistent
    inconsistent = df[column].apply(lambda x: type(x)).unique()
    if len(inconsistent) > 1:
        inconsistent_rows[column] = df[df[column].apply(lambda x: type(x)) != str]

# Step 3: Output rows with type inconsistencies
for col, rows in inconsistent_rows.items():
    print(f"Inconsistent rows in {col}:")
    print(rows)

# Step 4: Read again with specified data types (adjust as necessary)
dtype_dict = {
    'Column11': 'bool',
    'Column12': 'string',
    'Column13': 'string',
    'Column14': 'string',
    'Column17': 'string',
    'Column19': 'string',
    'Column20': 'string',
    'Column21': 'string'
}

df_final = pd.read_csv('leads.csv', dtype=dtype_dict)

# Now df_final will be loaded with the specified data types
