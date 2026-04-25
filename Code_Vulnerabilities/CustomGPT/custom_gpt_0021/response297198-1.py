
import pandas as pd

def check_mixed_types(file_path, columns):
    chunk_size = 1000  # Adjust depending on memory and file size
    for chunk in pd.read_csv(file_path, chunksize=chunk_size):
        for col in columns:
            print(f"Column: {col}, Unique types: {chunk[col].apply(type).unique()}")

# Specify the problematic columns and your file path
problematic_columns = [11, 12, 13, 14, 17, 19, 20, 21]  # Adjust for zero-based index
check_mixed_types('leads.csv', problematic_columns)
