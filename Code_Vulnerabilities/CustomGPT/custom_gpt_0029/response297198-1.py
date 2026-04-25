
import pandas as pd

# Approach 1: Identify problematic rows
# Read specific columns to check datatypes
cols_to_check = [11, 12, 13, 14, 17, 19, 20, 21]
data_preview = pd.read_csv('leads.csv', usecols=cols_to_check)

# Check for mixed types in each column
for col in data_preview.columns:
    mixed_type_rows = data_preview[~data_preview[col].apply(lambda x: isinstance(x, str) or isinstance(x, bool))]
    if not mixed_type_rows.empty:
        print(f"Mixed type values found in column {col}:")
        print(mixed_type_rows)

# Approach 2: Specify dtypes while reading
# Define column datatypes explicitly based on your knowledge
dtype_dict = {
    'column_11': 'bool',  # Example boolean column
    'column_12': 'str',
    'column_13': 'str',
    'column_14': 'str',
    # Include other columns as necessary
}

data = pd.read_csv('leads.csv', dtype=dtype_dict, low_memory=False)

# Check data
print(data.dtypes)
