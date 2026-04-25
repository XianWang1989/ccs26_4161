
dtypes = {
    'Column11': 'bool',
    'Column12': 'string',
    # Add the rest of your column types as needed
}

data = pd.read_csv('leads.csv', dtype=dtypes)
