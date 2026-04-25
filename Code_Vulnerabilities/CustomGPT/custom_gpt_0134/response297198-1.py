
import pandas as pd

# Load the CSV with a subset of columns to check for mixed types
df = pd.read_csv('leads.csv', usecols=[11, 12, 13, 14, 17, 19, 20, 21])

# Loop through each column to identify rows with mixed types
for col in df.columns:
    # Check the unique types in the column
    unique_types = df[col].apply(type).unique()
    if len(unique_types) > 1:
        print(f"Column {col} has mixed types: {unique_types}")
        # Print out rows with mixed types
        mixed_rows = df[~df[col].apply(lambda x: isinstance(x, unique_types[0]))]
        print(mixed_rows)
