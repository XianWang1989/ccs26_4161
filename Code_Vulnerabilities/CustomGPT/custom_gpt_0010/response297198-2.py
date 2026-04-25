
dtype_dict = {
    'Column11': 'bool',  # Replace with the correct column name
    'Column12': 'str',   # Ensure you replace with appropriate data types
    # Add other columns based on your data
}

data = pd.read_csv('leads.csv', dtype=dtype_dict)
