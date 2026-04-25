
# Define the datatypes for known columns
dtype_dict = {
    'Column11': 'bool',  # For example, Column 11
    'Column12': 'str',   # For the remaining columns
    'Column13': 'str',
    # ... add other columns as needed
}

df = pd.read_csv('leads.csv', dtype=dtype_dict)
