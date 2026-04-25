
import pandas as pd

# Read the CSV file with low_memory option
df = pd.read_csv('leads.csv', low_memory=False)

# Check data types of the specific problematic columns
problematic_cols = df.columns[[11, 12, 13, 14, 17, 19, 20, 21]]
print(df[problematic_cols].dtypes)

# Identify rows with mixed types in a specific column (example for column 11)
mixed_type_rows = df[~df[problematic_cols[0]].apply(lambda x: isinstance(x, (str, bool)))]
print(mixed_type_rows)
