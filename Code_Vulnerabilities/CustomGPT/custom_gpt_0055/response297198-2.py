
# Define data types for the columns (adjust based on your actual data)
dtype_dict = {
    'ColumnK': bool,
    # Add other columns and their types as needed
}

# Import the CSV while specifying dtypes
df = pd.read_csv('leads.csv', dtype=dtype_dict)

# Alternatively, to avoid DtypeWarning while still checking types:
df = pd.read_csv('leads.csv', low_memory=False)
