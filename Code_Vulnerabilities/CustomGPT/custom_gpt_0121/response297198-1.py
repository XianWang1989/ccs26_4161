
import pandas as pd

# Try to read the CSV while catching errors
try:
    df = pd.read_csv('leads.csv', error_bad_lines=False)  # Lets you skip problematic lines
except Exception as e:
    print(f"Error reading CSV: {e}")

# Check the data types of the columns
print(df.dtypes)

# Identify rows with mixed types
for col in df.columns:
    mixed_type_rows = df[col].apply(type).value_counts()
    if len(mixed_type_rows) > 1:
        print(f"Column '{col}' has mixed types: {mixed_type_rows}")
