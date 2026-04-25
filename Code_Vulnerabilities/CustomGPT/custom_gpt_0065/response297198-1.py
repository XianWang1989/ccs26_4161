
import pandas as pd

# Load specific columns as strings to avoid DtypeWarning
df = pd.read_csv('leads.csv', usecols=[11, 12, 13, 14, 17, 19, 20, 21], dtype=str)

# Check for unique values in each of the problematic columns
for col in df.columns:
    unique_values = df[col].unique()
    print(f'Unique values in {col}: {unique_values}')
