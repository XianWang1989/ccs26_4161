
dtypes = {
    'Column11': 'bool',
    'Column12': 'str',
    'Column13': 'str',
    # Add other columns with their respective dtypes
}

data = pd.read_csv('leads.csv', dtype=dtypes)
