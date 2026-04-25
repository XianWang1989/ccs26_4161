
dtype_dict = {
    'ColumnK': bool,  # Replace 'ColumnK' with actual column name
    'ColumnX': str,
    # Add other columns and their corresponding types
}

# Import CSV with specified dtypes
df = pd.read_csv('leads.csv', dtype=dtype_dict)
