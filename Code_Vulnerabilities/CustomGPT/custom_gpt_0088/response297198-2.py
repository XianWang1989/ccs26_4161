
dtype_spec = {
    'column_11': 'bool',   # Change 'column_11' to the actual name
    'column_12': 'str',    # Adjust accordingly
    'column_13': 'str',
    'column_14': 'str',
    'column_17': 'str',
    'column_19': 'str',
    'column_20': 'str',
    'column_21': 'str'
}

df = pd.read_csv('leads.csv', dtype=dtype_spec)
