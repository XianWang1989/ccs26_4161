
column_types = {
    'ColumnK': bool,  # Replace with the actual name of Column K
    # Define other columns with their respective types
    'ColumnX': str,
    # Add additional mappings as necessary
}

data = pd.read_csv('leads.csv', dtype=column_types)

# Alternatively, if you want to ignore the warning:
# data = pd.read_csv('leads.csv', low_memory=False)
