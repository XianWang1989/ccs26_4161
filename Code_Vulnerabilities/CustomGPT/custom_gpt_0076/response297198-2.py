
dtype_dict = {
    'Column11': bool,
    'Column12': str,
    'Column13': str,
    # Add more columns based on your data
}

df = pd.read_csv('leads.csv', dtype=dtype_dict)
