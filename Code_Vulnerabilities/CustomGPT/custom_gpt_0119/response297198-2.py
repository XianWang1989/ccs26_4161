
# Specify dtypes for columns
dtype_dict = {
    'column_11_name': 'bool',  # Replace with actual column name and desired dtype
    # Add other columns as needed
}

# Read CSV with specific dtypes
df = pd.read_csv('leads.csv', dtype=dtype_dict)
