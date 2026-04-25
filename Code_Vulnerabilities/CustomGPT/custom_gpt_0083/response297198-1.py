
import pandas as pd

# Load the CSV with on_bad_lines to skip errors
df = pd.read_csv('leads.csv', on_bad_lines='skip')

# Check for mixed types in the problematic columns
for col in df.columns:
    if df[col].dtype == 'object':
        mixed_types = df[col].apply(type).value_counts()
        if len(mixed_types) > 1:
            print(f"Column {col} has mixed types:\n{mixed_types}")

# You can also inspect specific columns if needed
print(df[['Column11', 'Column12']].head())  # Replace with actual column names
