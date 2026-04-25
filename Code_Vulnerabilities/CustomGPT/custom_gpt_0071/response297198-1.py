
import pandas as pd

# Load the CSV file with coercing errors
df = pd.read_csv('leads.csv', low_memory=False)

# Check the problematic columns
problematic_cols = ['Column11', 'Column12', 'Column13', 'Column14', 'Column17', 'Column19', 'Column20', 'Column21']
for col in problematic_cols:
    non_numeric = df[col][pd.to_numeric(df[col], errors='coerce').isna()]
    if not non_numeric.empty:
        print(f"Invalid entries in {col}:")
        print(non_numeric)
