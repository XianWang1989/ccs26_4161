
# Define the data types for the affected columns
dtype_dict = {
    'Column11': 'bool',
    'Column12': 'object',  # Change according to your knowledge of the data
    'Column13': 'object',
    'Column14': 'object',
    'Column17': 'object',
    'Column19': 'object',
    'Column20': 'object',
    'Column21': 'object'
}

# Read the CSV with specified data types
df = pd.read_csv('leads.csv', dtype=dtype_dict)

# Further examination if required
print(df.head())
