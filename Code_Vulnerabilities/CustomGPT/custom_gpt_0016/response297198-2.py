
dtype_dict = {
    11: 'bool',    # Column K as a boolean
    12: 'str',     # Assuming a string for column 12
    13: 'str',     # Assuming a string for column 13
    # Add other columns as necessary
}

df = pd.read_csv('leads.csv', dtype=dtype_dict)
