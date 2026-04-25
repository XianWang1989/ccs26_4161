
import pandas as pd

# Load the data with warning suppression
df = pd.read_csv('leads.csv', error_bad_lines=False)

# Check data types of the columns
print(df.dtypes)

# Find rows with mixed types in specific columns
for col in ['Column11', 'Column12', 'Column13', 'Column14']:
    mixed_types = df[~df[col].apply(lambda x: isinstance(x, (str, bool)))]
    print(f"Mixed types in {col}:")
    print(mixed_types)
