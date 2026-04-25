
import pandas as pd

# Read the CSV with all columns as object type
df = pd.read_csv('leads.csv', dtype='object')

# Check for mixed types in specific columns
mixed_type_rows = {}

for col in [11, 12, 13, 14, 17, 19, 20, 21]:  # Adjust as needed
    mixed_types = df[col].apply(type).value_counts()
    if len(mixed_types) > 1:  # More than one type in the column
        mixed_type_rows[col] = df[col]

# Show rows with mixed types
for col, rows in mixed_type_rows.items():
    print(f"Column {col} has mixed types:\n{rows[mixed_types > 1]}")
