
# Specify dtypes for the columns
dtype_dict = {
    11: 'bool',     # Assuming Column K is Boolean
    12: 'string',
    13: 'string',
    14: 'string',
    17: 'string',
    19: 'string',
    20: 'string',
    21: 'string'
}

# Load the CSV with specific dtypes
data = pd.read_csv('leads.csv', dtype=dtype_dict)

# Now you can also validate the types
print(data.dtypes)
