
import pandas as pd

# Read the CSV without low_memory option
df = pd.read_csv('leads.csv')

# Check for mixed types in specific columns
for col in df.columns[11:22]:  # Adjust column indices as needed
    print(f"Unique types in {col}: {df[col].apply(type).unique()}")
