
import pandas as pd

# Load the CSV file with only the necessary columns to minimize memory usage
df = pd.read_csv('leads.csv', usecols=[11, 12, 13, 14, 17, 19, 20, 21], low_memory=False)

# Check the data types of each column
for col in df.columns:
    print(f"Column: {col}, Dtype: {df[col].dtype}, Unique values: {df[col].unique()}")

# Further analysis to identify rows that do not match expected types
for col in df.columns:
    if col == 'expected_boolean_column':  # adjust as needed
        problematic_rows = df[~df[col].isin(['TRUE', 'FALSE'])]
        print(f"Problematic rows in {col}:\n{problematic_rows}")
