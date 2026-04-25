
dtypes = {
    'column1': 'str',   # Change to your actual column names and types
    'column2': 'bool',
    # Add other columns with correct types
}
df = pd.read_csv('leads.csv', dtype=dtypes)
