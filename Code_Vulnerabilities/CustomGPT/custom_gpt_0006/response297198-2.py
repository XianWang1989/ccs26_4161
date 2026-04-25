
# Define the data types for specific columns
dtypes = {
    'Column11': 'bool',   # Adjust the column names accordingly
    'Column12': 'string',
    'Column13': 'string',
    # Add other columns as needed
}

# Read the CSV using specified dtype
df = pd.read_csv('leads.csv', dtype=dtypes, low_memory=False)
