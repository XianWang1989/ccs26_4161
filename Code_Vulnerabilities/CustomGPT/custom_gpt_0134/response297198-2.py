
# Define the column data types
dtype_dict = {
    'Column11': 'bool',   # Adjust according to your actual column names
    'Column12': 'str',
    'Column13': 'str',
    'Column14': 'str',
    'Column17': 'str',
    'Column19': 'str',
    'Column20': 'str',
    'Column21': 'str'
}

# Read the CSV file with specified dtypes
df = pd.read_csv('leads.csv', dtype=dtype_dict)
