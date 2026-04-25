
import pandas as pd

# Read a portion of the data to check types
sample_df = pd.read_csv('leads.csv', nrows=100)

# Check dtypes of the problematic columns
print(sample_df[['Column11', 'Column12', 'Column13']].dtypes)

# Identify rows with non-standard types
for col in ['Column11', 'Column12', 'Column13']:
    # Check for non-boolean values in Column11 for example
    non_standard = sample_df[~sample_df[col].isin(['TRUE', 'FALSE'])]
    print(f'Non-standard values in {col}:')
    print(non_standard)
