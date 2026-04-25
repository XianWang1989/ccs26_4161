
import pandas as pd

# Define specific dtypes for each column
dtypes = {
    'ColumnK': 'bool',      # Column 11 (K)
    'Column12': 'str',      # Adjust as needed
    'Column13': 'str',
    # Add other columns with their respective dtypes
}

# Read CSV with specified dtypes
df = pd.read_csv('leads.csv', dtype=dtypes, low_memory=False)

# Check the DataFrame
print(df.head())
