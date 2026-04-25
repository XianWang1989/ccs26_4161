
import pandas as pd

# Read a small portion of the file to inspect data types
sample_data = pd.read_csv('leads.csv', nrows=100)

# Check the data types of specific columns
for col in sample_data.columns[11:22]:  # Adjust the range as needed
    print(f"Column: {col} - Unique types: {sample_data[col].apply(type).unique()}")
