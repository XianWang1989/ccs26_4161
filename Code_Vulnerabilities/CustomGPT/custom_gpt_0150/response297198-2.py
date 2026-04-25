
dtype_dict = {
    'Column11': 'bool',
    'Column12': 'str',
    # Specify as needed...
}

df = pd.read_csv('leads.csv', dtype=dtype_dict)
