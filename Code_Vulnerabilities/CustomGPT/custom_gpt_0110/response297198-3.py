
import pandas as pd

# Define dtypes for specific columns
dtype_dict = {
    'Column11': 'bool',
    'Column12': 'str',
    'Column13': 'str',
    # Add other columns as necessary
}

# Load the CSV with specified dtypes
data = pd.read_csv('leads.csv', dtype=dtype_dict)

# Check for any missing values or inconsistencies
print(data.isnull().sum())

# Check the final data types
print(data.dtypes)
