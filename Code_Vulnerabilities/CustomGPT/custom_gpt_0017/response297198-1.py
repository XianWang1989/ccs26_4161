
import pandas as pd

# Define a function to check for mixed types in specified columns
def check_mixed_types(file_path, columns):
    for chunk in pd.read_csv(file_path, chunksize=1000):
        for col in columns:
            mixed_types = chunk[col].apply(type).value_counts()
            if len(mixed_types) > 1:
                print(f'Mixed types in column "{col}": {mixed_types}')

# Specify the columns to check (11, 12, 13, 14, 17, 19, 20, 21)
columns_to_check = ['Column_11', 'Column_12', 'Column_13', 'Column_14', 'Column_17', 'Column_19', 'Column_20', 'Column_21']
check_mixed_types('leads.csv', columns_to_check)
