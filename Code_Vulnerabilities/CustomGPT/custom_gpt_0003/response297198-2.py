
# Specify dtype for each column
dtype_spec = {
    'ColumnK': bool,  # Assuming Column 11 is Boolean
    'Column12': str,
    'Column13': str,
    # Add other columns with appropriate data types
}

leads_df = pd.read_csv('leads.csv', dtype=dtype_spec)

# Checking data types after conversion
print(leads_df.dtypes)
