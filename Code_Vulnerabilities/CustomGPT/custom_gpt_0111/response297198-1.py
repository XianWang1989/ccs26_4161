
import pandas as pd

# Define the columns to check for mixed types
columns_to_check = [11, 12, 13, 14, 17, 19, 20, 21]  # Use zero-based indices

# Read CSV in chunks
chunk_size = 1000
for chunk in pd.read_csv('leads.csv', chunksize=chunk_size):
    for col in columns_to_check:
        # Check for mixed types
        mixed_types = chunk[col].apply(type).value_counts()
        if len(mixed_types) > 1:
            print(f"Mixed types found in column {col}: {mixed_types}")
