
# Define dtypes for columns
dtypes = {
    'Column_11': 'bool',
    'Column_12': 'str',
    'Column_13': 'str',
    'Column_14': 'str',
    'Column_17': 'str',
    'Column_19': 'str',
    'Column_20': 'str',
    'Column_21': 'str'
}

# Read CSV with specified dtypes
df = pd.read_csv('leads.csv', dtype=dtypes)

# If reading fails, you can use low_memory=False
# df = pd.read_csv('leads.csv', dtype=dtypes, low_memory=False)
