
dtype_spec = {
    'ColumnK': bool,
    'ColumnX': str,
    'ColumnY': str,
    'ColumnZ': str,
    # add more columns as needed with their expected types
}

data = pd.read_csv('leads.csv', dtype=dtype_spec)
