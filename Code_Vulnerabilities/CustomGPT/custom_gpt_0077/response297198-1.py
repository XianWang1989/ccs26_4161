
import pandas as pd

# Read the CSV with specific columns set to string
df = pd.read_csv('leads.csv', usecols=[11, 12, 13, 14, 17, 19, 20, 21], dtype=str)

# Check for non-boolean values in Column 11
boolean_issue = df[df[11].notnull() & ~df[11].isin(['TRUE', 'FALSE'])]
print("Rows with issues in Column 11:")
print(boolean_issue)

# If you want to check for other columns with inconsistencies
for col in df.columns[1:]:  # Check all except the first column for mixed types
    mixed_types = df[col].apply(type).value_counts()
    print(f"\nColumn {col} types:")
    print(mixed_types)
