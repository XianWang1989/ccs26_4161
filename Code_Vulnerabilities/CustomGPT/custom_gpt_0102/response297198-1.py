
import pandas as pd

# Define a function to check for mixed types
def check_mixed_types(file_path):
    mixed_rows = []
    for chunk in pd.read_csv(file_path, chunksize=1000):
        for col in chunk.columns:
            if chunk[col].dtype == 'object':
                # Check types in the column
                types = chunk[col].apply(type).unique()
                if len(types) > 1:
                    mixed_rows.extend(chunk[chunk[col].apply(type).isin(types)].index.tolist())
    return set(mixed_rows)

file_path = 'leads.csv'
mixed_rows = check_mixed_types(file_path)

print(f"Rows with mixed types: {mixed_rows}")
