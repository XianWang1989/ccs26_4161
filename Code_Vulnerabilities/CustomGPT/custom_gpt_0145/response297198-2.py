
import pandas as pd

# Define dtypes for specific columns
dtype_dict = {
    'Column11': 'bool',   # Assuming Column11 is a Boolean
    'Column12': 'str',    # Adjust based on actual data type
    'Column13': 'str',
    'Column14': 'str',
    'Column17': 'str',
    'Column19': 'str',
    'Column20': 'str',
    'Column21': 'str',
}

# Read the CSV with specified dtypes
df = pd.read_csv('leads.csv', dtype=dtype_dict)

# Now, you shouldn't see any DtypeWarning
