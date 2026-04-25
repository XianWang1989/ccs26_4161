
import pandas as pd

# Define the dtype for each problematic column
dtype_specification = {
    'ColumnNameK': 'bool',  # Replace with actual column name for column 11
    'ColumnName12': 'str',  # Update with appropriate column name/types
    'ColumnName13': 'str',
    'ColumnName14': 'str',
    'ColumnName17': 'str',
    'ColumnName19': 'str',
    'ColumnName20': 'str',
    'ColumnName21': 'str'
}

# Import CSV with specified dtypes and low_memory set to False
leads_df = pd.read_csv('leads.csv', dtype=dtype_specification, low_memory=False)

# Identify rows causing issues, if any
for col in dtype_specification.keys():
    if leads_df[col].dtype == 'object':  # Check for object types that may contain mixed types
        inconsistent_rows = leads_df[~leads_df[col].isin(leads_df[col].dropna().unique())]
        print(f"Inconsistent rows in {col}:")
        print(inconsistent_rows)
