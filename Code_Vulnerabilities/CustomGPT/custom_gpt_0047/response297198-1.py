
import pandas as pd

# Load the data while specifying dtypes for known columns
dtypes = {
    'column_11': 'bool',
    # Specify other columns as necessary
}

# Initially read a sample of the data to check types
sample = pd.read_csv('leads.csv', dtype=dtypes, nrows=100)

# Now read the entire CSV with low_memory set to False to inspect the types
full_data = pd.read_csv('leads.csv', low_memory=False)

# Check for mixed types
mixed_type_rows = full_data[full_data['column_11'].apply(lambda x: isinstance(x, bool)) == False]

print(mixed_type_rows)
