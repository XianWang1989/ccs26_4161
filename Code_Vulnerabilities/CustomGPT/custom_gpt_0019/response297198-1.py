
import pandas as pd

# Load the CSV with specified dtype for problematic columns
df = pd.read_csv('leads.csv', usecols=[11, 12, 13, 14, 17, 19, 20, 21], low_memory=False)

# Check for mixed types
for col in df.columns:
    print(f"Column '{col}' unique types: {df[col].apply(type).unique()}")

# Display the rows that have mixed types
mixed_types = {}
for col in df.columns:
    mixed_types[col] = df[col].apply(type).nunique() > 1

# Identify rows with mixed types
rows_with_issues = df[mixed_types]
print(rows_with_issues)
