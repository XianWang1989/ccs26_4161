
# Specify column types explicitly
dtype_dict = {
    'column11': 'bool',  # Replace with actual column names and types
    'column12': 'str',
    'column13': 'str'
}

data = pd.read_csv('leads.csv', dtype=dtype_dict)

print(data.dtypes)
