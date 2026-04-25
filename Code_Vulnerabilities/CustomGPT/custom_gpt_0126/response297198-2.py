
dtype_dict = {
    'Column11': 'bool',
    'Column12': 'str',
    'Column13': 'str',
    'Column14': 'str'
}

df = pd.read_csv('leads.csv', dtype=dtype_dict, low_memory=False)
