
dtype_mapping = {
    # Adjust to your actual data types
    'column_11': 'bool',      # Column K as Boolean
    'column_12': 'str',       # Replace with column names from your CSV
    'column_13': 'str',
    'column_14': 'str',
    # Add rest of the columns as needed
}

# Read CSV with explicit dtype mapping
df = pd.read_csv('leads.csv', dtype=dtype_mapping, low_memory=False)

print(df.head())
