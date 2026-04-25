
# Specify data types for the problematic columns
dtype_spec = {
    'Column_K': bool,   # Replace with actual column name
    'Column_X': str,    # Replace with actual column name
    # Add other columns accordingly
}

# Read the CSV with specified dtypes
data = pd.read_csv('leads.csv', dtype=dtype_spec)

print(data.head())
