
dtype_dict = {
    11: 'bool',      # Column K as boolean
    12: 'str',       # Assuming string type for the rest
    13: 'str',
    14: 'str',
    17: 'str',
    19: 'str',
    20: 'str',
    21: 'str',
}

# Read the CSV while specifying dtype
df = pd.read_csv('leads.csv', dtype=dtype_dict)
