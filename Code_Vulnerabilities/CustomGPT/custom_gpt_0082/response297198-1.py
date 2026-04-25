
import pandas as pd

# Load the CSV file with all columns as strings
data = pd.read_csv('leads.csv', dtype=str)

# Check for any NaN values in the specific columns causing issues
mixed_type_rows = data[[11, 12, 13, 14, 17, 19, 20, 21]].apply(lambda x: x.str.contains('TRUE|FALSE', na=False).all(), axis=1)

# Display problematic rows
problematic_rows = data[~mixed_type_rows]
print(problematic_rows)
