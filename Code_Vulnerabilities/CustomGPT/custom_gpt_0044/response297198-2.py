
dtype_dict = {
    'Column11': 'bool',  # Adjust as necessary
    'Column12': 'str',  # Adjust as necessary
    'Column13': 'str',  # etc.
    # Add more columns as needed
}

df = pd.read_csv('leads.csv', dtype=dtype_dict, low_memory=False)
