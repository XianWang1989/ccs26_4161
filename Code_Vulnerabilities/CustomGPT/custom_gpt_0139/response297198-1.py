
import pandas as pd

# Load the CSV with a specific dtype for the problematic columns.
# Adjust the dtypes as per your columns (e.g., boolean, string)
dtypes = {
    'Column11': 'bool',
    'Column12': 'string',
    'Column13': 'string',
    'Column14': 'string',
    'Column17': 'string',
    'Column19': 'string',
    'Column20': 'string',
    'Column21': 'string'
}

# Read the CSV, setting low_memory=False to avoid warnings
df = pd.read_csv('leads.csv', dtype=dtypes, low_memory=False)

# Display rows with problematic types
print(df[['Column11', 'Column12', 'Column13', 'Column14', 'Column17', 'Column19', 'Column20', 'Column21']].applymap(type))
