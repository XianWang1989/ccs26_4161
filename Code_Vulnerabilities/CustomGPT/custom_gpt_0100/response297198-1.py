
import pandas as pd

# Load the CSV with low_memory set to False to avoid warnings
data = pd.read_csv('leads.csv', low_memory=False)

# Check the unique types in the specified columns
problematic_columns = [11, 12, 13, 14, 17, 19, 20, 21]
for col in problematic_columns:
    print(f"Column {col} unique types:")
    print(data.iloc[:, col].apply(type).unique())
