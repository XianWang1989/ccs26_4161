
# Define the dtype for each problematic column
dtype_dict = {
    'Column_K': 'bool',  # For Boolean
    'Column_12': 'str',  # Adjust as necessary
    # Add other columns and their respective types
}

# Read the CSV with specified dtypes
data = pd.read_csv('leads.csv', dtype=dtype_dict, low_memory=False)

# Alternatively, to ignore DtypeWarning
# data = pd.read_csv('leads.csv', low_memory=False)
