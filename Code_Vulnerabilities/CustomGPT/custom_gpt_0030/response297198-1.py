
import pandas as pd

# Load only the problematic columns to check their types
leads_df = pd.read_csv('leads.csv', usecols=[11, 12, 13, 14, 17, 19, 20, 21], low_memory=False)

# Check the data types in each column
for col in leads_df.columns:
    print(f"Column {col} unique types: {leads_df[col].apply(type).unique()}")
