
import pandas as pd

# Read the CSV with all columns as strings
df = pd.read_csv('leads.csv', dtype=str)

# Check the unique values in the problematic columns
problematic_columns = [11, 12, 13, 14, 17, 19, 20, 21]

for col in problematic_columns:
    print(f"Unique values in column {col}: {df.iloc[:, col].unique()}")
