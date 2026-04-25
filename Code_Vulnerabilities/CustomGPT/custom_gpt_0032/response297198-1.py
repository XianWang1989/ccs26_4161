
import pandas as pd

# Read the CSV with low_memory=False
df = pd.read_csv('leads.csv', low_memory=False)

# Check for mixed types in the specified columns
problematic_columns = ['col11', 'col12', 'col13', 'col14', 'col17', 'col19', 'col20', 'col21']

# Identify rows with mixed types
for col in problematic_columns:
    mixed_type_rows = df[~df[col].apply(lambda x: isinstance(x, (str, bool)))]
    if not mixed_type_rows.empty:
        print(f"Rows with mixed types in {col}:")
        print(mixed_type_rows)
