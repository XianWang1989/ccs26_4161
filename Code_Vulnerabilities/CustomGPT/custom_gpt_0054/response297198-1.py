
import pandas as pd

# Load the CSV without specifying low_memory for initial inspection
df = pd.read_csv('leads.csv', low_memory=False)

# Check the unique data types in the specified columns
for col in [11, 12, 13, 14, 17, 19, 20, 21]:  # Adjust index based on zero-based index
    print(f"Column {col} - Unique Types: {df.iloc[:, col].apply(type).unique()}")
