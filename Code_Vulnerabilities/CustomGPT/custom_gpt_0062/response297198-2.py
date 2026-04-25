
# Specify dtypes for columns explicitly
dtypes = {
    'ColumnK': 'bool',
    'ColumnL': 'string',  # Adjust according to other columns
    # Add other columns with their corresponding types
}

# Load the CSV with specified dtypes
df = pd.read_csv('leads.csv', dtype=dtypes)

# Verify the data types
print(df.dtypes)
