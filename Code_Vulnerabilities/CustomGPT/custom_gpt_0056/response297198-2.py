
# Declare dtypes for the columns you know
dtypes = {
    'column_11': 'bool',       # Assuming column 11 is boolean
    'column_12': 'str',        # Assuming column 12 is a string
    # Add similar entries for other problematic columns
}

df = pd.read_csv('leads.csv', dtype=dtypes, low_memory=False)
