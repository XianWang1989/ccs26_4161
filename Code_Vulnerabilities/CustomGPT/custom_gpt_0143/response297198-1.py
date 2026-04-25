
import pandas as pd

# Load the CSV file with dtype as object
df = pd.read_csv('leads.csv', dtype='object')

# Check the data types of each column
print(df.dtypes)

# Identify rows with mixed types
for col in ['Column_11', 'Column_12', 'Column_13']:  # Replace with actual column names
    mixed_rows = df[pd.to_numeric(df[col], errors='coerce').isna()]
    if not mixed_rows.empty:
        print(f'Mixed type rows in {col}:')
        print(mixed_rows)
