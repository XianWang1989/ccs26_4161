
dtype_dict = {
    'col11': 'bool',
    'col12': 'str',
    'col13': 'str',
    'col14': 'str',
    'col17': 'str',
    'col19': 'str',
    'col20': 'str',
    'col21': 'str'
}

df = pd.read_csv('leads.csv', dtype=dtype_dict)
