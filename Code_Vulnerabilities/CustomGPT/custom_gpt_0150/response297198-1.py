
import pandas as pd

# Step 1: Load the CSV file with low_memory option
df = pd.read_csv('leads.csv', low_memory=False)

# Step 2: Identify columns with mixed types
mixed_type_cols = df.columns[df.dtypes.eq(object) & df.applymap(lambda x: isinstance(x, str) or pd.isna(x)).any()]

# Step 3: Check unique types in the mixed type columns
for col in mixed_type_cols:
    unique_types = df[col].apply(type).unique()
    print(f"Column '{col}' has the following types: {unique_types}")

# Optionally, convert a specific column to a consistent type
df['Column11'] = df['Column11'].astype(bool)  # For a Boolean column
