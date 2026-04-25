
import pandas as pd

# Load the CSV with all columns as strings
leads_df = pd.read_csv('leads.csv', dtype=str)

# Check specific columns for unique values that may indicate type issues
for col in ['column_11', 'column_12', 'column_13']:  # Modify with actual column names
    print(f"Unique values in {col}: {leads_df[col].unique()}")
