
import pandas as pd

# Read the CSV file without dtype specification
data = pd.read_csv('leads.csv', low_memory=False)

# Check data types of each column
print(data.dtypes)

# Identify rows with mixed types in specific columns (e.g., Column 11)
mixed_type_rows = data[data['Column11'].apply(lambda x: isinstance(x, str) and x not in ['TRUE', 'FALSE'])]
print(mixed_type_rows)
