
import pandas as pd

# Load the CSV with dtype set to str for all columns
df = pd.read_csv('leads.csv', dtype=str)

# Check the data types of the columns
print(df.dtypes)

# Identify unique values in the problematic columns
for col in ['Column11', 'Column12', 'Column13', 'Column14', 'Column17', 'Column19', 'Column20', 'Column21']:
    print(f"Unique values in {col}: {df[col].unique()}")
