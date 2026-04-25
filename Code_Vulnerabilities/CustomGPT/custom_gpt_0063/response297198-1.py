
import pandas as pd

# Read the CSV with specific columns as strings
df = pd.read_csv('leads.csv', usecols=[11, 12, 13, 14, 17, 19, 20, 21], dtype=str)

# Check for unique values in each column to identify inconsistencies
for col in df.columns:
    print(f"Unique values in column {col}: {df[col].unique()}")
