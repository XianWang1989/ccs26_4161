
# Define the expected data types for the problematic columns
dtype_dict = {
    'Column11': 'bool',  # expected boolean
    'Column12': 'str',
    # Add more columns and their types based on your analysis
}

# Load the CSV with specified dtypes
df = pd.read_csv('leads.csv', dtype=dtype_dict)

# If you encounter errors with empty strings, consider filling them
df['Column11'] = df['Column11'].replace('', None).astype('bool')

# Check the dataframe 
print(df.info())
