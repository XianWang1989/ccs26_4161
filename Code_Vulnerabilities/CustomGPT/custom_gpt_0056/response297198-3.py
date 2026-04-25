
import pandas as pd

# Custom function to check for boolean values
def check_dtype(value):
    if isinstance(value, str) and value.strip() not in {'TRUE', 'FALSE', ''}:
        raise ValueError(f"Unexpected value: {value}")
    return value

# Attempt to load the CSV to identify issues
try:
    df = pd.read_csv('leads.csv', converters={11: check_dtype})
except ValueError as e:
    print(e)

# If no issues, specify dtypes for a clean import
dtypes = {
    'column_11': 'bool',
    'column_12': 'str',
    # Add remaining columns with known types
}

df = pd.read_csv('leads.csv', dtype=dtypes, low_memory=False)
