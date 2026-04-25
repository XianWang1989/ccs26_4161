
import pandas as pd

# Step 1: Check the data types by reading a limited number of rows
sample_data = pd.read_csv('leads.csv', nrows=100)
print(sample_data.dtypes)

# Step 2: Specify dtypes upon import
data_types = {
    'column_11': 'bool',  # Assuming column_11 is the Boolean column
    'column_12': 'string',  # Replace with actual column names and desired types
    # Add other columns as needed
}

# Importing the full dataset with specified dtypes
try:
    full_data = pd.read_csv('leads.csv', dtype=data_types)
except Exception as e:
    print("Error occurred:", e)

# Optional: Identify problematic rows
problematic_rows = pd.read_csv('leads.csv', skiprows=sample_data.index)
print(problematic_rows)
