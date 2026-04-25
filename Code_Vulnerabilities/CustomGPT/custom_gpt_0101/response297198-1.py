
import pandas as pd

# Load the CSV with low_memory option and inspect problematic columns
data = pd.read_csv('leads.csv', low_memory=False)

# Identify rows causing mixed types in specific columns
boolean_column_11 = pd.to_numeric(data.iloc[:, 11], errors='coerce')
mixed_rows = data[boolean_column_11.isna()]

# Display problematic rows
print(mixed_rows)

# Alternatively, specify dtypes directly
dtypes = {
    'column_name_11': 'bool',
    'column_name_12': 'str',  # replace with actual column names
    'column_name_13': 'str',
    # Continue for other columns as needed
}

data_with_dtypes = pd.read_csv('leads.csv', dtype=dtypes)
