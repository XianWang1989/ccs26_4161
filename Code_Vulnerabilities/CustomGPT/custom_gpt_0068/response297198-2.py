
# Define the data types for the columns
dtype_dict = {
    'ColumnK': 'bool', 
    'Column12': 'str', 
    'Column13': 'str', 
    'Column14': 'str', 
    'Column17': 'str', 
    'Column19': 'str', 
    'Column20': 'str', 
    'Column21': 'str'
}

# Read CSV specifying the dtypes
df = pd.read_csv('leads.csv', dtype=dtype_dict)

# Check the data types
print(df.dtypes)
