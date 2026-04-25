
dtype_mapping = {
    'ColumnK': 'bool',  # Example boolean column
    'ColumnX': 'str',   # Replace 'ColumnX' with actual column names
    'ColumnY': 'str',   # Adjust types as necessary
    # Add other columns according to their expected types
}

# Read the CSV with dtype specification
data = pd.read_csv('leads.csv', dtype=dtype_mapping)

print(data.head())
