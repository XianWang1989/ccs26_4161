
import pandas as pd

# Read the CSV file with all columns as strings
df = pd.read_csv('leads.csv', dtype=str)

# Identify problematic columns (e.g., columns 11 to 21)
problematic_cols = df.columns[11:22]

# Function to check types in each problematic column
for col in problematic_cols:
    mixed_types = df[col].apply(type).value_counts()
    print(f"Mixed types in column {col}:\n{mixed_types}\n")

# Optionally, check for unique values to find inconsistencies
for col in problematic_cols:
    print(f"Unique values in column {col}:\n{df[col].unique()}\n")
