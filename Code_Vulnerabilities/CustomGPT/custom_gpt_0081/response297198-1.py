
import pandas as pd

# Load the CSV with dtype=str
df = pd.read_csv('leads.csv', dtype=str)

# Check columns of interest for mixed types
columns_to_check = ['Column11', 'Column12', 'Column13', 'Column14', 
                    'Column17', 'Column19', 'Column20', 'Column21']

for column in columns_to_check:
    print(f"Unique values in {column}:")
    print(df[column].unique())
    print("\n")
