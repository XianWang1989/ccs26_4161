
dtype_dict = {
    'column_name_11': 'bool',   # Change to your actual column name
    'column_name_12': 'str',    # Change accordingly
    'column_name_13': 'str',
    'column_name_14': 'str',
    'column_name_17': 'str',
    'column_name_19': 'str',
    'column_name_20': 'str',
    'column_name_21': 'str',
}

# Read the CSV with specified dtypes
df = pd.read_csv('leads.csv', dtype=dtype_dict, low_memory=False)
