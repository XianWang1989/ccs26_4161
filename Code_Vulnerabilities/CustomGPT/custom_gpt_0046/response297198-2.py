
# Specify dtypes for columns directly
dtype_dict = {
    'Column11': 'bool',
    'Column12': 'str',
    'Column13': 'str',
    # Add other columns and their types as needed
}

# Read the CSV with the specified dtypes
df = pd.read_csv('leads.csv', dtype=dtype_dict, low_memory=False)

# If you expect some columns to have missing values, you might want to handle that
df.fillna('', inplace=True)  # Replace NaNs with empty strings or appropriate values
