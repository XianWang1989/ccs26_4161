
# Specify dtype for problematic columns
dtype_dict = {
    'ColumnK': 'bool',  # Adjust the column names and types accordingly
    # Add more columns as needed
}

# Load the CSV with specified dtypes
data = pd.read_csv('leads.csv', dtype=dtype_dict)

# Alternative: Ignore DtypeWarning and load without dtype
data = pd.read_csv('leads.csv', low_memory=False)
