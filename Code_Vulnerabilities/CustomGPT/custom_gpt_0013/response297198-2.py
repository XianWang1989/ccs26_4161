
# Specify data types while importing
dtype_dict = {
    'ColumnK': 'bool',  # Assuming ColumnK is a boolean
    'ColumnX': 'str',   # Adjust according to your columns
    # Add other columns as needed
}

data = pd.read_csv('leads.csv', dtype=dtype_dict)

# Alternatively, you can use low_memory=False
data = pd.read_csv('leads.csv', low_memory=False)
