
import pandas as pd

# Read the CSV with low_memory=False
df = pd.read_csv('leads.csv', low_memory=False)

# Identify mixed type columns
for col in df.columns:
    if df[col].dtype == 'object':
        mixed_types = df[col].apply(type).nunique() > 1
        if mixed_types:
            print(f"Column '{col}' has mixed types.")
            print(df[col].unique())  # Display unique types to inspect
