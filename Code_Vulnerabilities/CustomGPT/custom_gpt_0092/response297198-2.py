
# Load the CSV without specifying dtypes
data = pd.read_csv('leads.csv', low_memory=False)

# Identify mixed types in specified columns
for col in ['Column11', 'Column12', 'Column13']:  # Replace with actual column names
    mixed_rows = data[~data[col].isin([True, False])]  # Adjust condition for other types
    print(f'Mixed type rows in {col}:\n', mixed_rows)
