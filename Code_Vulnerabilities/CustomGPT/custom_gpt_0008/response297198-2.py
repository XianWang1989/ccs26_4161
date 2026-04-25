
dtype_mapping = {
    'Column11': 'bool',  # Replace with actual column names and types
    'Column12': 'string',
    'Column13': 'float',  # Use appropriate types based on data
    # Add other mappings as necessary
}

df = pd.read_csv('leads.csv', dtype=dtype_mapping)
