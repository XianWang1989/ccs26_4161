
dtype_dict = {
    'ColumnK': 'bool',  # Change to the appropriate types
    'Column12': str,
    'Column13': str,
    # continue for other columns...
}

df = pd.read_csv('leads.csv', dtype=dtype_dict)

# Inspect the data after loading
print(df.head())
