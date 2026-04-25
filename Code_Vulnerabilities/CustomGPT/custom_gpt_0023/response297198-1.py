
import pandas as pd

# Load the CSV while skipping problematic rows
try:
    data = pd.read_csv('leads.csv', error_bad_lines=False)
except Exception as e:
    print(e)

# Check the types of the specified columns
for col in [11, 12, 13, 14, 17, 19, 20, 21]:
    print(f"Column {col} type counts:")
    print(data.iloc[:, col].value_counts())
