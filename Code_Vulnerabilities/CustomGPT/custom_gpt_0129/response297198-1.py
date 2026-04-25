
import pandas as pd

# Load CSV with error handling
data = pd.read_csv('leads.csv', error_bad_lines=False)

# Check the data type of the problematic columns
problematic_columns = [11, 12, 13, 14, 17, 19, 20, 21]

# Check the unique data types in the problematic columns
for col in problematic_columns:
    print(f"Column {col} ({data.columns[col]}):")
    print(data.iloc[:, col].apply(type).value_counts())
    print("Unique entries:", data.iloc[:, col].unique())
