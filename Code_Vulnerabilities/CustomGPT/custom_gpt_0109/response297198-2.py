
dtype_dict = {
    'column_11': 'bool',  # Replace with actual column names
    'column_12': 'str',
    'column_13': 'str',
    # Add other columns as needed
}

data = pd.read_csv('leads.csv', dtype=dtype_dict)

# Alternatively, use low_memory=False but be mindful of performance issues.
# data = pd.read_csv('leads.csv', low_memory=False)
