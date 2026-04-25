
import pandas as pd

# Define a function to check for inconsistencies in specific columns
def check_column_types(file_path, columns):
    # Load the CSV in chunks
    chunk_size = 1000
    for chunk in pd.read_csv(file_path, chunksize=chunk_size):
        for col in columns:
            print(f"Column: {col}")
            inconsistent_rows = chunk[chunk[col].apply(type).nunique() > 1]
            if not inconsistent_rows.empty:
                print(inconsistent_rows)

# Specify the path to your CSV and columns to check
file_path = 'leads.csv'
columns_to_check = [11, 12, 13, 14, 17, 19, 20, 21] # Adjust the indexes based on your needs
check_column_types(file_path, columns_to_check)
