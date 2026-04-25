
import pandas as pd

# Load the CSV with a try-except block
try:
    data = pd.read_csv('leads.csv', low_memory=False)
except Exception as e:
    print(e)

# Check the types of the problematic columns
mixed_columns = [11, 12, 13, 14, 17, 19, 20, 21]
for col in mixed_columns:
    print(f"Column {col} types:\n{data.iloc[:, col].apply(type).value_counts()}\n")
