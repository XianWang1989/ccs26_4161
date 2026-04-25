
import pandas as pd

# Define the data types for each column to prevent mixed types
dtype_dict = {
    'Column11': 'bool',  # Assuming column K contains booleans
    'Column12': 'str',   # Defining types for other columns as required
    'Column13': 'str',
    'Column14': 'str',
    'Column17': 'str',
    'Column19': 'str',
    'Column20': 'str',
    'Column21': 'str',
}

# Try to load the CSV file with specified dtypes
try:
    df = pd.read_csv('leads.csv', dtype=dtype_dict)
except Exception as e:
    print(f"Error reading CSV: {e}")

# To identify problematic rows, check unique values in those columns
for col in dtype_dict.keys():
    if col in df.columns:
        print(f"Unique values in {col}: {df[col].unique()}")

# You can also filter out non-boolean entries from Column11 for verification
if 'Column11' in df.columns:
    problematic_rows = df[df['Column11'].apply(lambda x: x not in [True, False])]
    print("Rows with inconsistent boolean values:\n", problematic_rows)
