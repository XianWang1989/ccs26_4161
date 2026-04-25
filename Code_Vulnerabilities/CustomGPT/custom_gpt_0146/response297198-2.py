
# Define the data type for each problematic column explicitly
dtype_specification = {
    'ColumnK': 'bool',  # Assuming Column K is the 11th column named 'ColumnK'
    'Column12': 'str',
    'Column13': 'str',
    # Continue for other columns
    # ...
}

# Import with dtype specification
df = pd.read_csv(file_path, dtype=dtype_specification, low_memory=False)
