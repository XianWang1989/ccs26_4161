
import pandas as pd

# Define datatypes for problematic columns
dtype_mapping = {
    'ColumnK': 'bool',  # Example mapping for the Boolean field
    # Add mappings for other columns accordingly
}

# Reading the CSV with specific dtypes and low_memory=True (or False as per your preference)
df = pd.read_csv('leads.csv', dtype=dtype_mapping, low_memory=True)

# Check the DataFrame
print(df.dtypes)
