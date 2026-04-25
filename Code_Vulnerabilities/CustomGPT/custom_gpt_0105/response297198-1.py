
import pandas as pd

# Load your CSV file with warning suppression
try:
    df = pd.read_csv('leads.csv', low_memory=False)
except Exception as e:
    print(e)

# Check for mixed types by looking at unique values in the columns
for col in df.columns:
    print(f"Column: {col}, Unique types: {df[col].apply(type).unique()}")
