
import pandas as pd

# Load the CSV with a limited number of rows
sample_data = pd.read_csv('leads.csv', nrows=1000)

# Check the data types of the columns
print(sample_data.dtypes)

# Identify unique values in specific columns that have warnings
for col in [11, 12, 13, 14, 17, 19, 20, 21]:  # Adjust indices if needed
    print(f"Unique values in column {col}:")
    print(sample_data.iloc[:, col].unique())
