
# Specify column types
dtype_dict = {
    'ColumnK': 'bool',  # Example for #11
    # Add other columns as needed. E.g.:
    # 'Column12': 'str',
    # 'Column13': 'str',
}

# Import with defined dtypes
data = pd.read_csv('leads.csv', dtype=dtype_dict, low_memory=False)
