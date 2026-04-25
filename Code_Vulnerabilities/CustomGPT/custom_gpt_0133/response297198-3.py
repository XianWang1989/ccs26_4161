
dtype_dict = {
    'Column11': 'bool',  # Adjust the column names and types accordingly
    'Column12': 'str',
    'Column13': 'str',  # And so on for other problematic columns
    'Column14': 'str',
    # ...
}

df = pd.read_csv('leads.csv', dtype=dtype_dict)
