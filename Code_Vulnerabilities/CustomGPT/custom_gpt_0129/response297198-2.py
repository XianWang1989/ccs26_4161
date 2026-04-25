
# Define the dtypes for the specific columns
dtype_dict = {
    'column_name_11': 'bool',  # Replace 'column_name_11' with actual column name
    'column_name_12': 'str',   # Replace 'column_name_12' with actual column name
    # Repeat for all columns needing a dtype specified
}

# Load CSV with specified dtypes
data = pd.read_csv('leads.csv', dtype=dtype_dict)

# Optionally, you can also disable low_memory
# data = pd.read_csv('leads.csv', dtype=dtype_dict, low_memory=False)
