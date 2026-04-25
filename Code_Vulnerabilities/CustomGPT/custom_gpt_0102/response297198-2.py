
dtypes = {
    'Column11': 'bool',  # Column K
    'Column12': 'str',   # Adjust datatype for other columns accordingly
    'Column13': 'str',
    # Add other columns here
}

# Read the CSV with specified dtypes
data = pd.read_csv(file_path, dtype=dtypes)
