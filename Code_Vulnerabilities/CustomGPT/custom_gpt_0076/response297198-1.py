
import pandas as pd

# Load the CSV file without setting dtype
df = pd.read_csv('leads.csv', low_memory=False)

# Check the data types of the problematic columns
problematic_columns = df.columns[[11, 12, 13, 14, 17, 19, 20, 21]]

# Identify rows with mixed types
for column in problematic_columns:
    mixed_type_rows = df[~df[column].apply(lambda x: isinstance(x, str) or isinstance(x, bool))]
    if not mixed_type_rows.empty:
        print(f"Column '{column}' has mixed types in these rows:")
        print(mixed_type_rows)
