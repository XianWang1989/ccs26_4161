
# Define data types for specific columns
dtype_dict = {
    'Column11': 'bool',   # Assuming Column 11 is a Boolean
    'Column12': 'str',    # Replace with appropriate dtype
    'Column13': 'str',    # Continue for other columns
    # Add other columns as needed
}

# Read the CSV with specified dtypes
df = pd.read_csv('leads.csv', dtype=dtype_dict)

# If you're encountering issues, consider using low_memory=False as a last resort
# df = pd.read_csv('leads.csv', low_memory=False)
