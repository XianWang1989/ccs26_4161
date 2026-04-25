
import pandas as pd

# Load the CSV with all data as strings
data = pd.read_csv('leads.csv', dtype=str)

# Check columns with potential mixed types
suspect_columns = data.columns[[11, 12, 13, 14, 17, 19, 20, 21]]
mixed_type_rows = {}

for column in suspect_columns:
    # Identify unique types in each column
    unique_types = data[column].apply(type).unique()
    if len(unique_types) > 1:
        mixed_type_rows[column] = data[column]

# Display rows with mixed types
for column, rows in mixed_type_rows.items():
    print(f"Column {column} has mixed types:")
    print(rows[mixed_type_rows[column].isnull() | (rows != rows.astype(str))])
