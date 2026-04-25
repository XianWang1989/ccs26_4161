
dtype_dict = {
    'column_11': 'bool',
    'column_12': 'str',
    'column_13': 'int',
    # Add the correct types for all relevant columns
}

df = pd.read_csv('leads.csv', dtype=dtype_dict, low_memory=False)
