
import pandas as pd

# Use low_memory=False (optional) and specify the columns to avoid mixed types
df = pd.read_csv('leads.csv', low_memory=False, dtype={'Column11': 'object', 'Column12': 'object', 
                                                      'Column13': 'object', 'Column14': 'object', 
                                                      'Column17': 'object', 'Column19': 'object', 
                                                      'Column20': 'object', 'Column21': 'object'})

# Identify inconsistent entries
for column in df.columns:
    if df[column].dtype == 'object':  # Check only object columns
        print(f"Unique values in {column}: {df[column].unique()}")

# Or, to just find rows with non-boolean values in Column K
boolean_column = df['Column11']  # Change this based on your dataframe
invalid_rows = boolean_column[~boolean_column.isin(['TRUE', 'FALSE'])]

print("Invalid rows in Column K:\n", invalid_rows)
