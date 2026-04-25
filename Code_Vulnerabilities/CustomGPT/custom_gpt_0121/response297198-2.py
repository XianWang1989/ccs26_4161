
# Define the specific data types for your columns
dtype_spec = {
    'column_k': 'bool',  # Change 'column_k' to your actual column name
    # Define other columns based on your understanding of the data
}

# Read the CSV with the specified data types
df = pd.read_csv('leads.csv', dtype=dtype_spec, low_memory=False)
