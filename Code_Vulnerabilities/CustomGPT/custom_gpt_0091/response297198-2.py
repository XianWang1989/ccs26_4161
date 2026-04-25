
# Specify dtypes for your columns
dtype_dict = {
    11: 'bool',   # Adjust based on actual data type
    12: 'str',    # Example type
    13: 'str',
    14: 'str',
    17: 'str',
    19: 'str',
    20: 'str',
    21: 'str',
    # Add additional dtype specifications as needed
}

# Read the CSV with specified dtypes
df = pd.read_csv('leads.csv', dtype=dtype_dict)

# Alternatively, use low_memory=False
# df = pd.read_csv('leads.csv', low_memory=False)
