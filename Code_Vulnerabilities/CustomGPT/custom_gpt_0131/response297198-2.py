
dtype_dict = {
    'column_11': 'boolean',  # Example for a boolean field
    'column_12': 'str',      # Replace with actual types based on your data
    # add other columns as necessary
}

df = pd.read_csv('leads.csv', dtype=dtype_dict, low_memory=False)
