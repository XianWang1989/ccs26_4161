
import pandas as pd

# Attempt to read the CSV file
try:
    df = pd.read_csv('leads.csv', dtype=str, error_bad_lines=False)
except Exception as e:
    print("Error reading CSV:", e)

# Check for inconsistencies in specific columns
for col in ['Column_11', 'Column_12', 'Column_13', 'Column_14', 'Column_17', 'Column_19', 'Column_20', 'Column_21']:
    print(f"Inconsistent types in {col}:")
    print(df[col].apply(type).value_counts())
