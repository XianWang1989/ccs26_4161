
# Define dtype for each column based on expected data types
dtype_dict = {
    'ColumnK': 'bool',  # Assuming that column 11 is boolean
    'Column12': 'str',
    'Column13': 'str',
    'Column14': 'str',
    'Column17': 'str',
    'Column19': 'str',
    'Column20': 'str',
    'Column21': 'str'
}

# Load the CSV with specified dtypes
df = pd.read_csv('leads.csv', dtype=dtype_dict)

# Checking the datatypes to confirm
print(df.dtypes)
