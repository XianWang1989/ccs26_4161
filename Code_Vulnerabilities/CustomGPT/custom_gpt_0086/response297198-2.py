
dtype_dict = {
    'Column_11': 'bool',
    'Column_12': 'string',  # Adjust based on your needs
    'Column_13': 'string'
    # Add other columns with their appropriate types
}

data = pd.read_csv('leads.csv', dtype=dtype_dict)
