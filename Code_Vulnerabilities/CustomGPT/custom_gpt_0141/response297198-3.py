
dtype_dict = {
    'ColumnK': 'bool',  # Assuming Column 11 (K) is boolean
    'ColumnX': 'string',  # Other columns as strings, adjust as necessary
    'ColumnY': 'float',   # If you expect a numeric value
    # Add all relevant columns here with their expected types
}

df = pd.read_csv('leads.csv', dtype=dtype_dict)
