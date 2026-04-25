
import pandas as pd

# Function to check for mixed types in specific columns
def check_mixed_types(file_path, columns):
    mixed_rows = []
    for chunk in pd.read_csv(file_path, chunksize=1000):
        for col in columns:
            mixed_dtype = chunk[col].dtype
            if mixed_dtype == 'object':  # Checking for non-numeric types
                non_numeric = chunk[~chunk[col].apply(lambda x: isinstance(x, (int, float, bool)))].index.tolist()
                mixed_rows.extend(non_numeric)
    return set(mixed_rows)

# Columns to check (11, 12, 13, 14, 17, 19, 20, 21 are converted to zero-based index)
columns_to_check = [10, 11, 12, 13, 16, 18, 19, 20]  # 0-based indexing
mixed_rows = check_mixed_types('leads.csv', columns_to_check)

print(f'Rows with mixed types: {mixed_rows}')
