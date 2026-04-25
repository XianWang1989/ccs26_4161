
import pandas as pd

# Function to check mixed types in a specific column
def check_mixed_types(filepath, cols_to_check):
    for chunk in pd.read_csv(filepath, chunksize=1000):
        for col in cols_to_check:
            mixed_types = chunk[col].apply(type)
            if mixed_types.nunique() > 1:
                print(f"Mixed types found in column '{col}' in chunk:\n{chunk.loc[mixed_types != mixed_types.iloc[0]]}")

# Specify the columns to check (replace with your specific columns)
columns_to_check = [11, 12, 13, 14, 17, 19, 20, 21]
check_mixed_types('leads.csv', columns_to_check)
