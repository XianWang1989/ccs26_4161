
# Define data types for the problematic columns
dtypes = {
    'ColumnK': 'bool',  # Column 11 as boolean
    # Define other columns based on your knowledge of the data
    'Column12': 'string',
    'Column13': 'string',
    'Column14': 'string',
    # Continue for other columns...
}

# Now, import the CSV with specified dtypes
data = pd.read_csv('leads.csv', dtype=dtypes, low_memory=False)
