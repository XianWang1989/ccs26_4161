
# Define the dtype for each column
dtype_dict = {
    'ColumnK': 'bool',
    'Column12': 'string',
    'Column13': 'string',
    'Column14': 'string',
    'Column17': 'string',
    'Column19': 'string',
    'Column20': 'string',
    'Column21': 'string',
}

# Read the CSV with dtype specified and low_memory=False
data = pd.read_csv('leads.csv', dtype=dtype_dict, low_memory=False)
