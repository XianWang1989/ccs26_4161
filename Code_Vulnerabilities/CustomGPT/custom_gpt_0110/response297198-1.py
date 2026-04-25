
import pandas as pd

# Load the CSV without setting low_memory=False
data = pd.read_csv('leads.csv', low_memory=True)

# Check the dtype of the columns
print(data.dtypes)

# Identify rows with mixed types in specific columns
for column in ['Column11', 'Column12', 'Column13']:  # Replace with actual column names
    mixed_types = data[column].apply(type).value_counts()
    print(f"Mixed types in {column}:\n{mixed_types}\n")
