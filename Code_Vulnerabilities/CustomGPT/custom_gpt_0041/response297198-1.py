
import pandas as pd

# Read the CSV with error handling
df = pd.read_csv('leads.csv', error_bad_lines=False)

# Check the data types of each column
print(df.dtypes)

# Identify rows with mixed types in the problematic columns
for col in df.columns:
    if df[col].dtype == 'object':  # Check only object type columns
        mixed_type_rows = df[~df[col].apply(lambda x: isinstance(x, str)) & df[col].ffill().notnull()]
        if not mixed_type_rows.empty:
            print(f'Rows with mixed types in {col}:')
            print(mixed_type_rows)
