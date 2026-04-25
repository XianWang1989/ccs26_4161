
import pandas as pd

# Load the CSV with low_memory=True
df = pd.read_csv('leads.csv', low_memory=True)

# Check data types of the columns
print(df.dtypes)

# Identify problematic rows for a specific column (e.g., Column K)
# Replace 'ColumnK' with the actual column name or use df.iloc[:, 10] for the 11th column
mixed_rows = df[df['ColumnK'].apply(lambda x: isinstance(x, str) and x not in ['TRUE', 'FALSE'])]
print(mixed_rows)
