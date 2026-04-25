
# Load the CSV with low_memory set to False
df = pd.read_csv('leads.csv', low_memory=False)

# If you still face dtype issues, specify the dtype
# Example: if 'Column11' is Boolean
df = pd.read_csv('leads.csv', dtype={
    'Column11': 'bool',  # or 'int' if you want to convert TRUE/FALSE to 1/0
    'Column12': 'str',
    # Add other columns as necessary
})
