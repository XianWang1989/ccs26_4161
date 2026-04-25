
dtype_dict = {
    'Column11': 'bool',
    'Column12': 'str',
    'Column13': 'str',
    # Add other columns as needed
}

data = pd.read_csv('leads.csv', dtype=dtype_dict)
