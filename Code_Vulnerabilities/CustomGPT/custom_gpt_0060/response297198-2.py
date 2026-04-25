
# Define expected types for all columns
dtype_mapping = {
    'Column11': 'bool',
    'Column12': 'category',
    # Define appropriate types for other columns ...
}

data = pd.read_csv('leads.csv', dtype=dtype_mapping, low_memory=False)  # Adjust dtype_mapping as necessary
