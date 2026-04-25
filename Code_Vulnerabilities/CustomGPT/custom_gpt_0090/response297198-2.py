
# Define a dictionary of dtypes for the columns
dtype_dict = {
    'ColumnK': bool,
    'Column20': str,
    'Column21': str,
    # add more as needed
}

# Read CSV with specified dtypes
df = pd.read_csv('leads.csv', dtype=dtype_dict)

# Or with low_memory option (less preferred)
# df = pd.read_csv('leads.csv', low_memory=False)
