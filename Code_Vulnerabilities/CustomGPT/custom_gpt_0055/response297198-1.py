
import pandas as pd

# Function to identify rows with mixed types
def check_mixed_types(file_path):
    for chunk in pd.read_csv(file_path, chunksize=1000):
        for column in chunk.columns:
            mixed = chunk[column].apply(type).nunique() > 1
            if mixed:
                print(f"Column '{column}' has mixed types in the following rows:")
                print(chunk[chunk[column].apply(type) != chunk[column].dtype.type])

check_mixed_types('leads.csv')
