
import pandas as pd

# Define a function to identify problematic rows
def find_problematic_rows(file_path):
    problematic_rows = []
    # Read the CSV in chunks
    for chunk in pd.read_csv(file_path, chunksize=1000):
        for col in chunk.columns:
            if chunk[col].dtype == 'object':
                # Check for mixed types
                if len(chunk[col].unique()) > 1:
                    problematic_rows.extend(chunk[chunk[col].apply(lambda x: not isinstance(x, (bool, str, int)))].index.tolist())
    return set(problematic_rows)

problematic_indices = find_problematic_rows('leads.csv')
print("Problematic row indices:", problematic_indices)
