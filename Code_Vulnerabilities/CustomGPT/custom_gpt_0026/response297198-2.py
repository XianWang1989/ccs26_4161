
dtype_dict = {
    'Column11': 'bool',  # Adjust column names and types as needed
    'Column12': 'string',
    'Column13': 'string',
    # ... other columns with appropriate types
}

# Load the CSV and specify dtypes
df = pd.read_csv('leads.csv', dtype=dtype_dict, low_memory=False)

# Verify data types
print(df.dtypes)
