
import pandas as pd

# Define the dtypes dictionary based on your data understanding
dtype_dict = {
    11: 'bool',    # Column K assumed to be Boolean
    12: 'str',     # Column assumed to be String
    13: 'str',     # Column assumed to be String
    14: 'str',     # Column assumed to be String
    17: 'str',     # Column assumed to be String
    19: 'str',     # Column assumed to be String
    20: 'str',     # Column assumed to be String
    21: 'str'      # Column assumed to be String
}

# Load the CSV with specified dtype
df = pd.read_csv('leads.csv', dtype=dtype_dict)

# Perform your analysis
print(df.head())
