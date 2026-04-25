
import pandas as pd

# Load the CSV without specifying dtypes
data = pd.read_csv('leads.csv', low_memory=False)

# Check the problematic columns
problematic_columns = [11, 12, 13, 14, 17, 19, 20, 21]

# Function to identify rows with mixed types in specific columns
def identify_mixed_types(df, cols):
    for col in cols:
        mixed_type_rows = df[~df[col].apply(type).isin([str, bool])]
        if not mixed_type_rows.empty:
            print(f"Mixed type values found in column {col}:\n{mixed_type_rows}\n")

identify_mixed_types(data, problematic_columns)
