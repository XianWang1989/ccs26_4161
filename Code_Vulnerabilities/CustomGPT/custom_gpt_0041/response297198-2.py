
# Define the data types for each column
dtype_dict = {
    'Column11': 'bool',
    'Column12': 'str',
    'Column13': 'str',
    # Add other columns as necessary
}

# Read the CSV with specified dtypes
df = pd.read_csv('leads.csv', dtype=dtype_dict, low_memory=False)

# Check for any issues after loading
print(df.dtypes)
