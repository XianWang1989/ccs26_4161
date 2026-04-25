
import pandas as pd

# Read the CSV with all columns as strings
df = pd.read_csv('leads.csv', dtype=str)

# Check columns with mixed types
problematic_columns = ['Column11', 'Column12', 'Column13', 'Column14', 'Column17', 'Column19', 'Column20', 'Column21']

for column in problematic_columns:
    # Find unique values in the problematic columns
    unique_values = df[column].unique()
    print(f'Unique values in {column}: {unique_values}')
