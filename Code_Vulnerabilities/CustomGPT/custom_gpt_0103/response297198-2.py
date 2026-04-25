
# Specify data types for critical columns
dtypes = {
    11: 'boolean',
    12: 'str',
    13: 'str',
    # Add other columns as needed
}

df = pd.read_csv('leads.csv', dtype=dtypes)
