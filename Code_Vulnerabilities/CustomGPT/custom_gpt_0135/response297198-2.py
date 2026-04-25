
dtype_dict = {
    'column_11_name': 'bool',  # Replace with the actual column name
    # Include other columns with their appropriate data types
}

# Read the CSV with specified dtypes
data = pd.read_csv('leads.csv', dtype=dtype_dict)
