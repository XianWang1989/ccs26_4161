
# Define the data types for columns explicitly
dtypes = {
    'Column_K': 'bool',  # Specify correct type for Column K
    'Column_12': 'str',
    'Column_13': 'str',
    # Add other columns with their respective types as needed
}

# Import the CSV with specified dtypes
df = pd.read_csv('leads.csv', dtype=dtypes, low_memory=False)
