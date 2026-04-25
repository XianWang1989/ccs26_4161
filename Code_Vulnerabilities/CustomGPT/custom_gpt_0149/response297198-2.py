
# Specify dtypes for the problematic columns
dtypes = {
    'Column11': bool,  # Assuming this is Column K
    'Column12': str,
    'Column13': str,
    # Add others as needed...
}

# Load the CSV with specified dtypes
data = pd.read_csv('leads.csv', dtype=dtypes)

# If you want to ignore the warning
data = pd.read_csv('leads.csv', low_memory=False)
