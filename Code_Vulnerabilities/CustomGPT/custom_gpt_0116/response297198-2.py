
# Specify the dtype during import
dtype_dict = {
    'Column11': bool,      # Adjust with actual column names
    'Column12': str,
    'Column13': str,
    # Add other column types as needed
}

df = pd.read_csv('leads.csv', dtype=dtype_dict)
