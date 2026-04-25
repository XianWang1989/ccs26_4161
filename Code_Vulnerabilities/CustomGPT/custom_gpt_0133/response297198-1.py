
import pandas as pd

# Set an empty dataframe to concatenate chunks later
data = pd.DataFrame()

# Read the CSV file in chunks
for chunk in pd.read_csv('leads.csv', chunksize=1000):
    data = pd.concat([data, chunk], ignore_index=True)

# Checking the dtypes of columns
print(data.dtypes)

# Checking for mixed types in specific columns
for column in data.columns:
    unique_types = data[column].apply(type).unique()
    if len(unique_types) > 1:
        print(f"Column '{column}' has mixed types: {unique_types}")
