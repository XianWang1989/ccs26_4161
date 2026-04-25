
import pandas as pd

# Read CSV with specified options
df = pd.read_csv('leads.csv', on_bad_lines='skip')

# Check data types for specific columns
for col in df.columns[11:22]:  # Adjust as needed for your columns
    print(f"Column: {col} | Unique types: {df[col].apply(type).unique()}")
