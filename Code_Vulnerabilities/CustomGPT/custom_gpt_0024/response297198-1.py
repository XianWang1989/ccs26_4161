
import pandas as pd

def find_mixed_types(file_path, column_indices):
    mixed_rows = []

    for chunk in pd.read_csv(file_path, chunksize=1000):
        for index in column_indices:
            mixed_rows += chunk[chunk.iloc[:, index].apply(type).ne(type(chunk.iloc[:, index].iloc[0]))].index.tolist()

    return set(mixed_rows)

file_path = 'leads.csv'
column_indices = [11, 12, 13, 14, 17, 19, 20, 21]  # Adjust indices to zero-based
mixed_rows = find_mixed_types(file_path, column_indices)

if mixed_rows:
    print(f"Rows with mixed types: {mixed_rows}")
else:
    print("No mixed type rows found.")
