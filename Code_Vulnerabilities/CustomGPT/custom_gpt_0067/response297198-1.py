
import pandas as pd

# Read a small portion of the data to identify issues
sample_data = pd.read_csv('leads.csv', nrows=100)

# Check specific columns for mixed types
problematic_columns = [11, 12, 13, 14, 17, 19, 20, 21]
for col in problematic_columns:
    print(f"Column {col} unique values:")
    print(sample_data.iloc[:, col].unique())
