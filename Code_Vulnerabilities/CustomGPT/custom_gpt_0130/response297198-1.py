
import pandas as pd

# Read only the columns of concern
columns_of_interest = [11, 12, 13, 14, 17, 19, 20, 21]
data = pd.read_csv('leads.csv', usecols=columns_of_interest)

# Check the data types of each column
print(data.dtypes)

# Find rows with mixed types
for col in data.columns:
    mixed_rows = data[~data[col].apply(lambda x: isinstance(x, str) or isinstance(x, bool))]
    if not mixed_rows.empty:
        print(f'Mixed type rows in column {col}:')
        print(mixed_rows)
