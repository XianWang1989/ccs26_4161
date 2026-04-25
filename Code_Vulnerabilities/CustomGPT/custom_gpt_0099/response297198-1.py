
import pandas as pd

# Read the CSV with a small subset of rows to identify issues
sample_df = pd.read_csv('leads.csv', nrows=1000)

# Check the types of the problematic columns
problematic_columns = sample_df.columns[[11, 12, 13, 14, 17, 19, 20, 21]]
mixed_type_rows = sample_df[problematic_columns].applymap(type).nunique() > 1

# Display rows where mixed types are found
mixed_type_rows = sample_df[mixed_type_rows.any(axis=1)]
print(mixed_type_rows)
