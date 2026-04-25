
import pandas as pd

# Define the dtypes for columns to avoid mixed type warnings
dtypes = {
    'Column11': 'bool',  # boolean for column K (index 11)
    'Column12': 'str',   # string for column L (index 12)
    # Define other column types as needed
}

# Read the CSV specifying dtypes and low_memory option
df = pd.read_csv('leads.csv', dtype=dtypes, low_memory=False)

print(df.info())  # Check dtypes
