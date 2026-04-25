
import pandas as pd

# Define the function to check for inconsistent types
def check_column_types(file_path, columns):
    chunks = pd.read_csv(file_path, chunksize=1000)
    for chunk in chunks:
        for col in columns:
            print(f"Column: {col}")
            print(chunk[col].apply(type).value_counts())
            print("-" * 40)

# List the problematic columns
problematic_columns = [11, 12, 13, 14, 17, 19, 20, 21]  # Adjust as needed
check_column_types('leads.csv', problematic_columns)
