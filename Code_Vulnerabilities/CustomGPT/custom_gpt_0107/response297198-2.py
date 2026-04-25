
# Define data types for specific columns
dtype_dict = {
    'ColumnK': 'bool',  # Assuming Column 11 is a Boolean
    # Add other columns with appropriate dtypes
}

df = pd.read_csv(file_path, dtype=dtype_dict)

# Alternatively, set low_memory=False (not recommended for large files)
# df = pd.read_csv(file_path, low_memory=False)
