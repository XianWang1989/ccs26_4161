
import pandas as pd

# Read the CSV with low_memory=True (the default)
df = pd.read_csv('leads.csv', low_memory=True)

# Check data types
print(df.dtypes)

# Inspect specific columns for mixed types
for col in df.columns[11:22]:  # Columns 11 to 21
    print(f'Column: {col}\n')
    print(df[col].unique())  # Show unique values to identify issues
    print('\n')
