
dtype_dict = {
    'column_11': bool,
    'column_12': str,
    'column_13': str,
    'column_14': str,
    'column_17': str,
    'column_19': str,
    'column_20': str,
    'column_21': str
}

data = pd.read_csv('leads.csv', dtype=dtype_dict, low_memory=False)
