
dtype_dict = {
    'Column11': 'boolean',  # Set to bool for True/False
    'Column12': 'str',      # String for alphanumeric fields
    'Column13': 'str',      # Adjust based on your needs
}

# Read the CSV with explicit data types
df = pd.read_csv('leads.csv', dtype=dtype_dict)

# Now you can check the dataframe and confirm types
print(df.dtypes)
