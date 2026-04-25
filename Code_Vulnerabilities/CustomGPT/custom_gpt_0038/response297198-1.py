
import pandas as pd

# Load only the problematic columns to identify issues
problematic_columns = [11, 12, 13, 14, 17, 19, 20, 21]
data = pd.read_csv('leads.csv', usecols=problematic_columns)

# Check the data types of each column
print(data.dtypes)

# Find rows with inconsistent types
for col in data.columns:
    inconsistent_rows = data[~data[col].apply(lambda x: isinstance(x, (str, bool)))]
    print(f"Inconsistent rows in column {col}:")
    print(inconsistent_rows)
