
import pandas as pd

# Attempt to read the CSV, allowing bad lines
df = pd.read_csv('leads.csv', error_bad_lines=False)

# Check data types of the columns
print(df.dtypes)

# Identify problematic rows
for col in df.columns:
    if df[col].apply(type).nunique() > 1:  # Check for mixed types
        print(f"Column '{col}' has mixed types.")
        print(df[col].dropna().unique())  # Show unique types in that column
