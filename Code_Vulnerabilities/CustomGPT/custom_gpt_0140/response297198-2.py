
# Specify the expected dtypes
dtype_dict = {
    'column_name_11': 'bool',  # Update with your actual column name
    'column_name_12': 'str',    # Repeat for other columns
    # Add other columns as needed
}

# Load CSV while specifying dtypes
df = pd.read_csv('leads.csv', dtype=dtype_dict)

# Check the data types to confirm
print(df.dtypes)
