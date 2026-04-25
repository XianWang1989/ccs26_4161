
dtype_dict = {
    'Column11': 'bool',
    'Column12': 'str',
    'Column13': 'str',
    'Column14': 'str',
    'Column17': 'str',
    'Column19': 'str',
    'Column20': 'str',
    'Column21': 'str'
}

df = pd.read_csv('leads.csv', dtype=dtype_dict)
