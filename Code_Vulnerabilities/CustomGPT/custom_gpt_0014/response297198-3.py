
dtype_spec = {
    'Column11': 'bool',
    'Column12': 'str',
    'Column13': 'str',
    # Add other columns as necessary
}

df = pd.read_csv('leads.csv', dtype=dtype_spec)
