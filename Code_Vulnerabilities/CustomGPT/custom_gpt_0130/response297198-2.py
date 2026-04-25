
dtype_dict = {
    'Column11': 'bool',  # Change to actual column name
    'Column12': 'str',   # Adjust as necessary
    # Add all relevant columns
}

data = pd.read_csv('leads.csv', dtype=dtype_dict)
