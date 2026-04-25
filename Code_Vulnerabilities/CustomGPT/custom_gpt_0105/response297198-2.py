
# Define column types explicitly
dtype_dict = {
    'column_name_11': 'bool',  # Assuming column K is a boolean
    # Add other column names and their expected types
}

df = pd.read_csv('leads.csv', dtype=dtype_dict)
