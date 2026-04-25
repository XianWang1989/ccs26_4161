
dtype_dict = {
    'ColumnK': 'bool',  # Example for column 11
    'Column12': 'str',
    'Column13': 'str',
    # Add other columns as needed
}

df = pd.read_csv('leads.csv', dtype=dtype_dict)
