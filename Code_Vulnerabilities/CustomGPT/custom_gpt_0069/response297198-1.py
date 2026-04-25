
import pandas as pd

# First, let's identify mixed types in the problematic columns
def check_mixed_types(file_path, columns):
    for chunk in pd.read_csv(file_path, usecols=columns, chunksize=1000):
        for col in columns:
            mixed_types = chunk[col].apply(type).nunique() > 1
            if mixed_types:
                print(f"Mixed types detected in column '{col}'")

# Specify the columns that were flagged
problematic_columns = [11, 12, 13, 14, 17, 19, 20, 21]
check_mixed_types('leads.csv', problematic_columns)

# Now, let's import the CSV with defined data types
dtypes = {
    'ColumnK': 'bool',  # Example: replace with actual column name
    'Column12': 'str',  # Adjust based on your data
    'Column13': 'str',
    # Add more columns here as necessary
}

# Read the CSV, specifying dtypes and low_memory=False
data = pd.read_csv('leads.csv', dtype=dtypes, low_memory=False)

print(data.dtypes)  # To verify datatypes after loading
