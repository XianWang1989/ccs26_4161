
column_types = {
    'column_name_11': 'bool',  # Change to actual column names
    'column_name_12': 'str',    # Provide the correct types
    # Add other column types as necessary
}

data = pd.read_csv('leads.csv', dtype=column_types)
