
import pandas as pd

# Load the data with all columns as object type
data = pd.read_csv('leads.csv', dtype='object')

# Check the specific columns for issues
problematic_rows = data[data.iloc[:, 11].str.contains('TRUE|FALSE', na=False) == False]

# Display rows that are problematic in Column 11
print(problematic_rows)
