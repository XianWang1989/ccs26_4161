
dtype_dict = {
    'ColumnK': 'bool',  # Specify the correct column names
    'ColumnL': 'str',
    # Continue for other columns referenced in the warning
}

# Import CSV with defined dtypes
data = pd.read_csv('leads.csv', dtype=dtype_dict, low_memory=False)

# Alternatively, you could read it without specifying dtypes
# and inspect the data types after import:
data = pd.read_csv('leads.csv', low_memory=False)

# Check data types
print(data.dtypes)
