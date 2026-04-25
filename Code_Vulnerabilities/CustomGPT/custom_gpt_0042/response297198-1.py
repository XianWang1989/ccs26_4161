
import pandas as pd

# Load the data with low_memory=False
df = pd.read_csv('leads.csv', low_memory=False)

# Check the data types of each column
print(df.dtypes)

# Identify rows with mixed types in specific columns
for col in ['Column11', 'Column12', 'Column13']:  # replace with actual column names
    mixed_rows = df[~df[col].apply(lambda x: isinstance(x, str) or isinstance(x, bool))]
    print(f"Mixed type rows in {col}:\n", mixed_rows)
