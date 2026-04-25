
import pandas as pd

# Read the CSV with a reduced number of rows to check type inconsistencies
sample_data = pd.read_csv('leads.csv', nrows=1000)

# Check data types for specific columns
for col in sample_data.columns:
    print(f"Column: {col}, Dtypes: {sample_data[col].apply(type).unique()}")
