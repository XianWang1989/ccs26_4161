
# Specify dtypes for the problematic columns
dtype_dict = {
    'Column11': bool,
    'Column12': str,
    'Column13': str,
    'Column14': str,
    'Column17': str,
    'Column19': str,
    'Column20': str,
    'Column21': str
}

# Import the CSV with specified dtypes
data = pd.read_csv('leads.csv', dtype=dtype_dict, low_memory=False)
