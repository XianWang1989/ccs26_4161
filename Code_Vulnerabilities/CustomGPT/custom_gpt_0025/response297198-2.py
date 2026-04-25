
# Define data types for the problematic columns
dtype_specifications = {
    'ColumnK': 'bool',
    'ColumnX': 'string',
    # Add other columns here
}

# Import CSV with specified dtypes
data = pd.read_csv('leads.csv', dtype=dtype_specifications)

# Alternative: Set low_memory
# data = pd.read_csv('leads.csv', low_memory=False)
