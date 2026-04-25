
# Specify dtype for columns if known
dtype_dict = {
    'column_name_11': bool,
    'column_name_12': str,
    'column_name_13': str,
    # Add all other columns accordingly
}

df = pd.read_csv('leads.csv', dtype=dtype_dict)

# If you're unsure of the column names, you can use the index position to specify
df = pd.read_csv('leads.csv', dtype={11: bool, 12: str, 13: str, 14: str, 17: str, 19: str, 20: str, 21: str})
