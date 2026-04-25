
import pandas as pd

# Load CSV with specific dtypes for problematic columns
dtypes = {
    'Column11': 'str',  # Change 'Column11' to the actual column name
    'Column12': 'str',  # Repeat for each column causing the DtypeWarning
    'Column13': 'str',
    'Column14': 'str',
    'Column17': 'str',
    'Column19': 'str',
    'Column20': 'str',
    'Column21': 'str'
}

# Read the CSV
df = pd.read_csv('leads.csv', dtype=dtypes)

# Inspect unique values in the problematic columns
for col in dtypes.keys():
    print(f"Unique values in {col}: {df[col].unique()}")
