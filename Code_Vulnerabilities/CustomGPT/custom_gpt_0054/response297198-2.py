
# Specify the dtype for the columns if known
dtypes = {
    'column_name_11': bool,    # Replace with actual column names
    'column_name_12': str,
    'column_name_13': str,
    # ... add other columns as needed
}

df = pd.read_csv('leads.csv', dtype=dtypes)
