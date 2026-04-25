
import pandas as pd

# Read the CSV file with low_memory=True to isolate problematic columns
df = pd.read_csv('leads.csv', low_memory=True)

# Check the types of each column in the DataFrame
for col in ['ColumnK', 'Column12', 'Column13', 'Column14', 'Column17', 'Column19', 'Column20', 'Column21']:
    print(f"Column: {col}")
    print(df[col].apply(type).value_counts())
    print("\n")
