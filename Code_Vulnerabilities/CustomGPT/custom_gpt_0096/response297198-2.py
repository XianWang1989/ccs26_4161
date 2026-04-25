
dtype_dict = {
    'Column11': 'bool',
    'Column12': 'str',
    'Column13': 'int',
    # Add more columns as necessary
}

df = pd.read_csv('leads.csv', dtype=dtype_dict)

# For columns that might have blanks, you may specify with 'object'
# df['ColumnWithBlanks'] = df['ColumnWithBlanks'].astype('object')
