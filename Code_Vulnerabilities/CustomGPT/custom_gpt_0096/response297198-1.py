
import pandas as pd

# Read the CSV file with error handling
try:
    df = pd.read_csv('leads.csv', error_bad_lines=False)
except Exception as e:
    print(f"Error: {e}")

# Check the data types of the columns
print(df.dtypes)

# Display rows with potential issues in specific columns
mixed_type_rows = df[df[['Column11', 'Column12', 'Column13']].applymap(type).nunique(axis=1) > 1]
print(mixed_type_rows)
