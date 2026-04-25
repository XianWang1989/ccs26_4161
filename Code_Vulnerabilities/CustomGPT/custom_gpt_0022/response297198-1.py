
import pandas as pd

# Read the CSV with error handling
df = pd.read_csv('leads.csv', error_bad_lines=False)

# Check data types of problematic columns
mixed_type_columns = [11, 12, 13, 14, 17, 19, 20, 21]
for col in mixed_type_columns:
    print(f"Column {col} unique types: {df.iloc[:, col].apply(type).unique()}")
