
import pandas as pd

# Load the data with an initial read (without low_memory=False)
df = pd.read_csv('leads.csv', low_memory=False)

# Check for mixed types in the specified columns
cols_to_check = ['Column11', 'Column12', 'Column13', 'Column14', 'Column17', 'Column19', 'Column20', 'Column21']

# Identifying and printing rows with mixed types
for col in cols_to_check:
    mixed_type_rows = df[~df[col].apply(lambda x: isinstance(x, (str, bool)))].index
    if mixed_type_rows.any():
        print(f'Rows in {col} with mixed types:', mixed_type_rows.tolist())
