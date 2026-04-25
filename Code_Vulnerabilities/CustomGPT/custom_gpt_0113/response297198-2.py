
# Specify the dtype for the problematic columns
dtype_dict = {
    'column_name_11': 'bool',  # replace with actual column name
    'column_name_12': 'str',    # replace with actual column name
    # Add dtypes for other columns based on what you're expecting
}

data = pd.read_csv('leads.csv', dtype=dtype_dict, low_memory=False)
