
data = pd.read_csv('leads.csv', dtype={
    'Column_K': 'bool',  # Adjust to your actual column names
    'Another_Column': 'str',
    # Add more mappings as necessary
})
