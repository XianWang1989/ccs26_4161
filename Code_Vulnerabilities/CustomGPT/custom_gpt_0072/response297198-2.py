
dtype_dict = {
    'ColumnK': 'bool',
    'ColumnX': 'str',   # Replace 'ColumnX', with actual column names and types
}

df = pd.read_csv('leads.csv', dtype=dtype_dict)
