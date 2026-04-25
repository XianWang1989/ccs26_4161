
# Define data types
dtypes = {
    'Column11': 'bool',  # adjust according to actual names
    'Column12': 'str',
    'Column13': 'str',
    # Add other columns as necessary
}

# Read the CSV with specified data types
df = pd.read_csv('leads.csv', dtype=dtypes)
