
dtype_mapping = {
    11: 'bool',  # Column K - Boolean
    12: 'str',   # Other columns - String
    13: 'str',
    14: 'str',
    17: 'str',
    19: 'str',
    20: 'str',
    21: 'str',
}

# Import the CSV with specified dtypes
df = pd.read_csv('leads.csv', dtype=dtype_mapping, low_memory=False)
