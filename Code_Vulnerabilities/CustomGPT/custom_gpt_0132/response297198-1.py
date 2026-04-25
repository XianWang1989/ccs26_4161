
import pandas as pd

# Load only the problematic columns
leads_df = pd.read_csv('leads.csv', usecols=[11, 12, 13, 14, 17, 19, 20, 21])

# Check for unique data types in each column
for column in leads_df.columns:
    print(f"Column {column}: {leads_df[column].apply(type).unique()}")
