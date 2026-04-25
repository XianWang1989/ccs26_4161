
import pandas as pd

# Read the CSV with specific columns as object type to avoid DtypeWarning
df = pd.read_csv('leads.csv', dtype={'Column11': 'object', 'Column12': 'object', 'Column13': 'object', 
                                      'Column14': 'object', 'Column17': 'object', 'Column19': 'object', 
                                      'Column20': 'object', 'Column21': 'object'})

# Check for inconsistencies
for column in df.columns:
    if df[column].dtype == 'object':  # Check only object columns
        print(f"Unique values in {column}: {df[column].unique()}")
