
dtypes = {
    'Column_11': 'bool',  # Replace with the actual column names
    'Column_12': 'str',
    'Column_13': 'str',
    'Column_14': 'str',
    'Column_17': 'str',
    'Column_19': 'str',
    'Column_20': 'str',
    'Column_21': 'str'
}

df = pd.read_csv('leads.csv', dtype=dtypes, low_memory=False)
