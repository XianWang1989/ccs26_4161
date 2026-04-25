
import pandas as pd

# Load a few rows to inspect the data
sample_data = pd.read_csv('leads.csv', nrows=100)
print(sample_data.dtypes)  # Check data types of each column
