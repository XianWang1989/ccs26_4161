
import pandas as pd

# Function to check for mixed types in specified columns
def check_mixed_types(file_path, columns_to_check):
    for chunk in pd.read_csv(file_path, chunksize=1000):
        for col in columns_to_check:
            print(f'Column: {col}')
            print(chunk[col].apply(type).value_counts())

# Specify the columns that are causing the mixed type warning
columns_with_issues = [11, 12, 13, 14, 17, 19, 20, 21]  # Adjust based on 0-indexing
file_path = 'leads.csv'
check_mixed_types(file_path, columns_with_issues)
