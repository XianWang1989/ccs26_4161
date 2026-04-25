
dtype_mapping = {
    'Column11': 'bool',  # Adjust with your actual column names
    'Column12': 'str',
    'Column13': 'str',
    # Add other columns as needed
}

# Read the CSV with specified types
df = pd.read_csv('leads.csv', dtype=dtype_mapping)

# If there are any missing values, you might want to handle them.
df.fillna('', inplace=True)  # Example for handling NAs
