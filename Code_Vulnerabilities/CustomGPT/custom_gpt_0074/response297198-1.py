
import pandas as pd

# Load the data with default settings
df = pd.read_csv('leads.csv')

# Check the data types of columns that are problematic (e.g., columns 11 to 21)
problematic_columns = [11, 12, 13, 14, 17, 19, 20, 21]
for col in problematic_columns:
    print(f"Column {col} Type: {df.iloc[:, col].apply(type).unique()}")
