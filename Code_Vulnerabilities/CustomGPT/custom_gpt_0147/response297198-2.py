
dtype_dict = {
    'Column11': 'bool',   # Change as needed
    'Column12': 'str',    # Assuming column 12 has strings
    # ... specify other columns based on data type
}

df = pd.read_csv('leads.csv', dtype=dtype_dict)
