
import pandas as pd

# Load the CSV file with just the problematic columns to check types
leads_df = pd.read_csv('leads.csv', usecols=[11, 12, 13, 14, 17, 19, 20, 21], low_memory=False)

# Checking data types in the selected columns
print(leads_df.dtypes)

# Find rows in each column that have different types
for col in leads_df.columns:
    print(f"Unique types in column '{col}': {leads_df[col].map(type).unique()}")
