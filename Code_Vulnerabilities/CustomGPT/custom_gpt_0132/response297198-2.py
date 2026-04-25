
# Specify dtypes for the problematic columns
dtypes = {
    'ColumnK': 'bool',  # replace with actual column name if needed
    'Column12': 'str',  # example types, adjust accordingly
    'Column13': 'str',
    'Column14': 'str',
    'Column17': 'str',
    'Column19': 'str',
    'Column20': 'str',
    'Column21': 'str',
}

# Import csv with specified dtypes
leads_df = pd.read_csv('leads.csv', dtype=dtypes)
