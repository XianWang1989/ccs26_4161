
import pandas as pd

# Load the CSV with a try-except block
try:
    df = pd.read_csv('leads.csv')
except Exception as e:
    print(f"Error reading CSV: {e}")

# Check for mixed types in the specified columns
for col in [11, 12, 13, 14, 17, 19, 20, 21]:
    # Convert column index to column name
    col_name = df.columns[col]

    # Try converting to string and check for unique types
    unique_types = df[col_name].apply(type).unique()
    if len(unique_types) > 1:
        print(f"Mixed types found in column {col_name}: {unique_types}")
