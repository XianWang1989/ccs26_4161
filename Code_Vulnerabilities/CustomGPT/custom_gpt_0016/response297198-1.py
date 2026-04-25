
import pandas as pd

def find_mixed_types(filename, columns):
    mixed_rows = []
    for chunk in pd.read_csv(filename, chunksize=1000):
        for col in columns:
            if col in chunk:
                if chunk[col].apply(type).nunique() > 1:  # Check for mixed types
                    mixed_rows.extend(chunk[chunk[col].apply(type) != chunk[col].dtype.type].index.tolist())
    return set(mixed_rows)  # Return unique indices

# Example usage
filename = 'leads.csv'
mixed_type_columns = [11, 12, 13, 14, 17, 19, 20, 21]
mixed_rows_index = find_mixed_types(filename, mixed_type_columns)
print("Rows with mixed types:", mixed_rows_index)
