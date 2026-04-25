
import pandas as pd

# Load the CSV with all columns as strings
df = pd.read_csv('leads.csv', dtype=str)

# Check for unique values in the problematic columns
problematic_columns = ['Column11', 'Column12', 'Column13', 'Column14', 'Column17', 'Column19', 'Column20', 'Column21']
for column in problematic_columns:
    unique_values = df[column].unique()
    print(f'Unique values in {column}: {unique_values}')
