
import pandas as pd

# Read the CSV with low_memory set to True to avoid loading all data types at once
df = pd.read_csv('leads.csv', low_memory=True)

# Check the data types of the columns of interest
print(df.dtypes)

# Identify rows with mixed types in specific columns
problematic_columns = [11, 12, 13, 14, 17, 19, 20, 21]  # Adjust index if needed
for col in problematic_columns:
    mixed_type_rows = df[df.iloc[:, col].apply(type) != df.iloc[:, col].dtype.type]
    print(f"Mixed type rows in column {col}:")
    print(mixed_type_rows)
