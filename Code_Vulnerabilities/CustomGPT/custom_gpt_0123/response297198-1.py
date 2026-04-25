
import pandas as pd

# Load only a few rows
data = pd.read_csv('leads.csv', nrows=100)

# Check the data types for the problematic columns
print(data.dtypes)

# Identify mixed type entries by checking each column
mixed_rows = {}
for column in data.columns[11:22]:  # Adjust range as needed
    mixed_rows[column] = data[column].apply(type).value_counts()

# Display mixed type information
print(mixed_rows)
