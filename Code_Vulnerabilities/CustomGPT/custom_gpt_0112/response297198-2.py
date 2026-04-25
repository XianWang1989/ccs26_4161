
# Specify dtypes for the columns
dtypes = {
    'Column11': bool,        # Example for Boolean
    'Column12': str,         # String fields
    # Repeat for other columns as needed
}

df = pd.read_csv('leads.csv', dtype=dtypes)

# Alternatively, you can ignore the warning if the data is still usable
# But bear in mind that it's best to identify the reasons for the warning
