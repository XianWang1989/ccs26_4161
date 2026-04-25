
# Define data types for each column
dtype_dict = {
    11: 'bool',
    12: 'str',
    13: 'str',
    14: 'str',
    17: 'str',
    19: 'str',
    20: 'str',
    21: 'str',
}

# Read the CSV with specified dtypes
df = pd.read_csv('leads.csv', dtype=dtype_dict)
