
import pandas as pd

# Load the CSV file with a subset of columns
leads = pd.read_csv('leads.csv', usecols=[11, 12, 13, 14, 17, 19, 20, 21], low_memory=False)

# Check the data types of these columns
for col in leads.columns:
    print(f"Column: {col}, Dtype: {leads[col].dtype}")

# Identify inconsistent types
for col in leads.columns:
    inconsistent_rows = leads[~leads[col].apply(lambda x: isinstance(x, (int, float, str, bool)))]
    if not inconsistent_rows.empty:
        print(f"Inconsistent rows in column {col}:")
        print(inconsistent_rows)
