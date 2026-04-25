
# Specify dtypes explicitly
dtype_dict = {
    'ColumnK': 'bool',   # Replace with the actual name
    # Add other columns as needed
}

df = pd.read_csv('leads.csv', dtype=dtype_dict, low_memory=False)
