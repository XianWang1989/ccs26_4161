
dtype_mapping = {
    'ColumnK': 'bool',  # adjust for your actual column names
    'Column12': 'string',
    'Column13': 'string',
    # add other columns with their appropriate types
}

df = pd.read_csv('leads.csv', dtype=dtype_mapping)
