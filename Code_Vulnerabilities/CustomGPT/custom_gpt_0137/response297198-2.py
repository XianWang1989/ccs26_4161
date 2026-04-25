
# Define the dtype for specific columns
dtype_mapping = {
    'column_name_11': 'bool',  # Boolean columns
    'column_name_12': 'str',    # Strings where mixed types may occur
    # Define other columns as necessary
}

# Read the CSV with dtype specified
leads_df = pd.read_csv('leads.csv', dtype=dtype_mapping, low_memory=False)

# Verify the data types
print(leads_df.dtypes)
