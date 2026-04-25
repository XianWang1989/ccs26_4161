
dtype_dict = {
    'column_11': 'bool',       # Column K expected as boolean
    'column_12': 'str',        # Assuming Column L as string
    'column_13': 'str',        # Continue for other columns
    'column_14': 'str',
    'column_17': 'str',
    'column_19': 'str',
    'column_20': 'str',
    'column_21': 'str',
}

# Load the CSV with specified dtypes
leads_df = pd.read_csv('leads.csv', dtype=dtype_dict)
