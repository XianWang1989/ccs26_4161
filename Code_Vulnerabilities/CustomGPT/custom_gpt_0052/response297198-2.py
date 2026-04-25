
# Define dtypes for your columns
dtypes = {
    'ColumnK': bool,  # Column 11
    'Column12': str,
    'Column13': str,
    'Column14': str,
    'Column17': str,
    'Column19': str,
    'Column20': str,
    'Column21': str,
}

# Import CSV with specified dtypes
data = pd.read_csv('leads.csv', dtype=dtypes)

# Validate the import
print(data.dtypes)
