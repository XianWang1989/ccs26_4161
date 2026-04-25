
import pandas as pd

# Define a function to check for mixed types
def check_mixed_types(file_path):
    chunk_size = 1000  # Adjust as needed
    for chunk in pd.read_csv(file_path, chunksize=chunk_size, low_memory=False):
        for col in chunk.columns:
            unique_types = chunk[col].apply(type).unique()
            if len(unique_types) > 1:
                print(f'Mixed types found in column: {col}')
                print(chunk[col].unique())  # Show unique values

# Call the function
check_mixed_types('leads.csv')
