
# Specify dtype for specific columns
dtype_dict = {
    'Column_11': 'boolean',  # Change according to your actual column names/types
    'Column_12': 'string',
    'Column_13': 'string',
    # Add more columns as needed
}

# Load the CSV specifying dtype
df = pd.read_csv('leads.csv', dtype=dtype_dict)

print(df.dtypes)  # Check the data types after loading
