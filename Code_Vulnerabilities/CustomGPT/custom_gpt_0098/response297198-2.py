
dtype_mapping = {
    'Column11': 'bool',  # Boolean
    # Define data types for other columns as needed
}
df = pd.read_csv('leads.csv', dtype=dtype_mapping)
