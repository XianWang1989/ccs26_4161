
# Define the dtypes for each column
dtypes = {
    'Column11': 'bool',
    'Column12': 'str',
    'Column13': 'str',
    'Column14': 'str',
    'Column17': 'str',
    'Column19': 'str',
    'Column20': 'str',
    'Column21': 'str'
}

# Load the CSV using specific dtypes
df = pd.read_csv('leads.csv', dtype=dtypes)

# Handle NaN values if necessary
df.fillna('', inplace=True)  # If you want to replace NaN with empty strings
