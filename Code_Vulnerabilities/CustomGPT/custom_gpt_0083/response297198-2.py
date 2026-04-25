
# Define dtypes for specific columns
dtype_dict = {
    'Column11': 'bool',  # Assuming Column 11 (K) is Boolean
    # Add other columns with their respective dtypes
}

# Import the CSV with specified dtypes
df = pd.read_csv('leads.csv', dtype=dtype_dict)

# If unsure about dtypes, load without specifying first and then inspect or convert
print(df.dtypes)  # Check the data types after loading
