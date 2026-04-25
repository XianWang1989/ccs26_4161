
dtype_dict = {
    'column_11': 'bool',     # Change to actual column names
    'column_12': 'str',
    # Add other column types as needed
}

data = pd.read_csv('leads.csv', dtype=dtype_dict)
