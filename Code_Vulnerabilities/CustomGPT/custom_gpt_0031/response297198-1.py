
import pandas as pd

# Attempt to load the CSV with low_memory set to False
df = pd.read_csv('leads.csv', low_memory=False)

# Check data types of columns
print(df.dtypes)

# Identify rows with mixed types in specific columns
mixed_type_rows = df[df['ColumnK'].apply(lambda x: isinstance(x, str) and x not in ['TRUE', 'FALSE'])]
print(mixed_type_rows)
