
import pandas as pd

# Define dtypes for each column, including those that may have mixed types
dtype_dict = {
    'column_11': 'bool',
    'column_12': 'str',
    # Add other columns and their respective types
}

# Load the CSV with specified dtypes
data = pd.read_csv('leads.csv', dtype=dtype_dict)

# Check if the dtype warning still occurs
print(data.dtypes)
