
# Specify the data types of the problematic columns
dtype = {
    'Column11': 'bool',  # Replace with the actual column name
    'Column12': 'str',
    'Column13': 'str',
    'Column14': 'str',
    # Add others as necessary
}

# Import the CSV with specified dtypes
data = pd.read_csv('leads.csv', dtype=dtype, low_memory=False)
