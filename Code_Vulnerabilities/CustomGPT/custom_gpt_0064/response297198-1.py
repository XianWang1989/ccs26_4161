
import pandas as pd

# Load the CSV with error handling
data = pd.read_csv('leads.csv', on_bad_lines='skip')

# Check the data types of each column
print(data.dtypes)

# Find rows with mixed types in the problematic columns
for col in ['column11', 'column12', 'column13']:  # replace with actual column names
    mixed_type_rows = data[pd.to_numeric(data[col], errors='coerce').isnull()]
    print(f"Rows with mixed types in {col}:\n", mixed_type_rows)
