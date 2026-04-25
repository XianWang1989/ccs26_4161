
import pandas as pd

# Load the CSV with specific columns as strings
data = pd.read_csv('leads.csv', dtype=str)

# Check for unique values in the problematic columns
problematic_columns = [11, 12, 13, 14, 17, 19, 20, 21]
for col in problematic_columns:
    print(f"Unique values in column {col}: {data.iloc[:, col].unique()}")
