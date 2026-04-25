
# Specify data types for problematic columns
dtypes = {
    'column_11': 'bool',
    'column_12': 'str',
    'column_13': 'str',
    # Add other columns with their respective types
}

# Import the CSV with specified dtypes
leads_df = pd.read_csv('leads.csv', dtype=dtypes)

print(leads_df.info())
