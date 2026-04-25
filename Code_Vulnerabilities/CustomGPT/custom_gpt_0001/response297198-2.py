
# Specify the dtypes for the columns explicitly
dtypes = {
    11: 'bool',       # Assuming this is the Boolean column
    12: 'str',        # Adjust these according to your data structure
    13: 'str',
    14: 'str',
    17: 'str',
    19: 'str',
    20: 'str',
    21: 'str'
}

# Read the CSV with specified dtypes
data = pd.read_csv('leads.csv', dtype=dtypes)
