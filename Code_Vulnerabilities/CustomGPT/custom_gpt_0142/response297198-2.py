
# Specify the dtype for each column
dtype_dict = {
    11: 'bool',   # Column K as Boolean
    12: 'str',    # String column
    13: 'str',    # String column
    14: 'str',    # String column
    17: 'str',    # String column
    19: 'str',    # String column
    20: 'str',    # String column
    21: 'str'     # String column
}

# Load the CSV while specifying dtypes
df = pd.read_csv('leads.csv', dtype=dtype_dict)

# If you do not want to specify every column manually, you could do:
# df = pd.read_csv('leads.csv', low_memory=False)

# Check the DataFrame
print(df.head())
