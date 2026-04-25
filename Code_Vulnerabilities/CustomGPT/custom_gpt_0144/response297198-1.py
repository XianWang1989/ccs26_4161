import pandas as pd

# Read only the problematic column(s) as string
df = pd.read_csv("leads.csv", dtype={11: str})  # You can do this for each column throwing the warning

# Check the unique types in the column
print(df.iloc[:, 11].apply(type).value_counts())

# Optionally, view rows that aren't of the expected type (e.g., not str or bool)
non_str_rows = df[~df.iloc[:, 11].apply(lambda x: isinstance(x, str))]
print(non_str_rows)
