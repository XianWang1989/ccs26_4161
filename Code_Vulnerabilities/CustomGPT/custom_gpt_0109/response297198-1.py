
import pandas as pd

# Load the CSV with low_memory=False to avoid incomplete dtype inference
data = pd.read_csv('leads.csv', low_memory=False)

# Identify columns with mixed types
mixed_types = data.select_dtypes(include=['object']).columns
for col in mixed_types:
    print(f"Checking column: {col}")
    unique_values = data[col].unique()
    print(unique_values)
