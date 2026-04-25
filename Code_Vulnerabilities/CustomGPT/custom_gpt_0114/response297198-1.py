
import pandas as pd

# Read only the problematic columns
cols_to_check = [11, 12, 13, 14, 17, 19, 20, 21]
df = pd.read_csv('leads.csv', usecols=cols_to_check)

# Identify rows with mixed types
for col in df.columns:
    try:
        df[col].astype(bool)  # Attempt to convert to boolean
    except ValueError as e:
        print(f"Column {col} has inconsistent types:")
        print(df[col].unique())  # Display unique values in the column
