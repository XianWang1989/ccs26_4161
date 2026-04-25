
# Define your column data types
dtype_dict = {
    'Column11': 'bool',    # replace with the actual name
    'Column12': 'str',
    'Column13': 'str',
    'Column14': 'str',
    'Column17': 'str',
    'Column19': 'str',
    'Column20': 'str',
    'Column21': 'str'
}

# Import the CSV specifying the data types
df = pd.read_csv('leads.csv', dtype=dtype_dict)

# Alternatively, using low_memory=False
# df = pd.read_csv('leads.csv', low_memory=False)
