
# Specify the data types for the columns
dtype_dict = {
    'Column11': 'bool',
    'Column12': 'str',
    'Column13': 'str',
    # Include all relevant columns here
}

# Read the CSV and specify the dtypes
leads = pd.read_csv('leads.csv', dtype=dtype_dict)

print("Data loaded successfully without DtypeWarning")
