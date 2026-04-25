
# Define dtypes for specific columns
dtype_dict = {
    'Column11': 'bool',  # example for Boolean columns
    'Column12': 'string',
    'Column13': 'string',  # adjust according to actual data
    # Add all relevant columns with appropriate dtypes
}

# Load the CSV file with specified dtypes
leads = pd.read_csv('leads.csv', dtype=dtype_dict)

# Confirm data types
print(leads.dtypes)
