
import pandas as pd

# Load CSV with all data as strings
df = pd.read_csv('leads.csv', dtype=str)

# Check data types in each column
print(df.dtypes)

# Identify rows with non-Boolean values in Column K (e.g., Column 11)
problematic_rows = df[~df[df.columns[11]].isin(['TRUE', 'FALSE'])]
print("Problematic rows in Column K:")
print(problematic_rows)
