
import pandas as pd

# Read the CSV file with low_memory set to False to avoid the warning
data = pd.read_csv('leads.csv', low_memory=False)

# Check the data types of the columns
print(data.dtypes)

# Identify rows where the data types are mixed. 
# Let's assume you want to check for Column 11 (index 10)
mixed_type_rows = data[pd.to_numeric(data.iloc[:, 10], errors='coerce').isnull()]

# Print rows that have mixed types
print(mixed_type_rows)
