
# Specify the data types explicitly
dtypes = {
    'Column_11': 'bool',
    'Column_12': 'str',  # Adjust based on actual expected types
    'Column_13': 'str',
    'Column_14': 'str',
    'Column_17': 'str',
    'Column_19': 'str',
    'Column_20': 'str',
    'Column_21': 'str'
}

# Load the CSV with specified dtypes
df = pd.read_csv('leads.csv', dtype=dtypes)

# Now you can proceed with your analysis without warnings
print(df.head())
