
import pandas as pd

# Load the data with low_memory=True (default)
data = pd.read_csv('leads.csv')

# Check the data types of the specified columns
problematic_columns = [11, 12, 13, 14, 17, 19, 20, 21]
data_types = data.iloc[:, problematic_columns].apply(type)

# Identify any rows with inconsistent types
for col in problematic_columns:
    inconsistent_rows = data[data.iloc[:, col].apply(type) != data_types.iloc[:, col].iloc[0]]
    if not inconsistent_rows.empty:
        print(f"Inconsistent values found in column {col}:")
        print(inconsistent_rows)
