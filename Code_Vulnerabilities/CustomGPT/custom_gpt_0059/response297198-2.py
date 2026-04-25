
dtype_mapping = {
    'Column11': 'bool',  # Adjust based on your actual columns
    'Column12': 'str',
    # Add other columns as needed
}

# Read CSV with specified dtypes
data = pd.read_csv('leads.csv', dtype=dtype_mapping)

# If you still receive a warning, investigate specific columns further
