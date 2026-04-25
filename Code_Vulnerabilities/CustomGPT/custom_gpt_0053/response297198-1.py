
import pandas as pd

# Define the columns that are causing the warning
problematic_columns = [11, 12, 13, 14, 17, 19, 20, 21]

# Read the CSV in chunks
chunk_size = 1000  # Adjust based on file size
for chunk in pd.read_csv('leads.csv', chunksize=chunk_size):
    for col in problematic_columns:
        if chunk.iloc[:, col].dtype == 'object':  # Check for object type
            mixed_type_rows = chunk[chunk.iloc[:, col].apply(lambda x: isinstance(x, str) and x.lower() not in ['true', 'false'])]
            if not mixed_type_rows.empty:
                print(mixed_type_rows)
