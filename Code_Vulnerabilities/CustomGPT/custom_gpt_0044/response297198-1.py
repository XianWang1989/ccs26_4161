
import pandas as pd

# Read the CSV with specified columns as string to avoid DtypeWarning
df = pd.read_csv('leads.csv', dtype=str)

# Check unique values in the problematic columns
for col in df.columns[11:22]:  # Adjust the index based on your CSV structure
    print(f"Unique values for column {col}: {df[col].unique()}")
