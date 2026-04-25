
import pandas as pd

# Read a small sample of the CSV
sample_data = pd.read_csv('leads.csv', nrows=100)

# Check the data types of the problematic columns
print(sample_data.dtypes)

# Read the full CSV while capturing errors
full_data = pd.read_csv('leads.csv', error_bad_lines=False)

# Identify problematic rows in specific columns
for col in ['column_11', 'column_12']:  # Replace with your actual column names
    problematic_rows = full_data[~full_data[col].apply(lambda x: isinstance(x, (str, bool)))]
    print(f'Problematic rows in {col}:\n', problematic_rows)
