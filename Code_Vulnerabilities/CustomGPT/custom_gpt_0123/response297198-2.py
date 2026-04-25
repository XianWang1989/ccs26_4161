
dtype_dict = {
    'column_11': 'bool',  # True/False as boolean
    'column_12': 'string', # Assuming it's a string column
    # Add other columns as needed
}

data = pd.read_csv('leads.csv', dtype=dtype_dict)
