
import pandas as pd

# Specify the columns that raise the warning
problematic_columns = [11, 12, 13, 14, 17, 19, 20, 21]

# Read the file in chunks to identify problematic rows
chunk_size = 1000
for chunk in pd.read_csv('leads.csv', chunksize=chunk_size):
    for col in problematic_columns:
        non_string_values = chunk[chunk.iloc[:, col].apply(lambda x: not isinstance(x, str) and pd.notnull(x))]
        if not non_string_values.empty:
            print(f"Non-string values found in Column {col}:")
            print(non_string_values)

# Note that column indices in 'problematic_columns' are zero-indexed.
