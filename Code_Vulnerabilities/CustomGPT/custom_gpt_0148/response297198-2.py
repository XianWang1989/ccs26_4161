
# Specify dtypes explicitly for columns
dtypes = {
    'ColumnK': 'bool',    # Example for a boolean column
    'Column1': 'str',     # Change based on your actual column names and types
    # Add other columns and their appropriate dtypes
}

# Read CSV with specified dtypes
df = pd.read_csv('leads.csv', dtype=dtypes)
