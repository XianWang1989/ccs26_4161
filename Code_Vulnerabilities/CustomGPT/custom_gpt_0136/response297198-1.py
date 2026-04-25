
import pandas as pd

# Step 1: Identify problematic rows
chunk_size = 1000
chunks = []

# Read the CSV in chunks
for chunk in pd.read_csv('leads.csv', chunksize=chunk_size):
    chunks.append(chunk)
    # Check data types
    print(chunk.dtypes)

# Combine chunks for further analysis if needed
data = pd.concat(chunks)

# Function to find mixed types
def find_mixed_types(df, cols):
    mixed_type_rows = {}
    for col in cols:
        if df[col].dtype == 'object':  # Check for object type columns
            mixed_type_indices = df[col].apply(type).ne(df[col].iloc[0].__class__).idxmax()
            mixed_type_rows[col] = df.index[df.apply(lambda x: isinstance(x[col], str) and not x[col].isnumeric())]
    return mixed_type_rows

# Specify columns with mixed types
columns_to_check = [11, 12, 13, 14, 17, 19, 20, 21]
mixed_rows = find_mixed_types(data, columns_to_check)
print(mixed_rows)

# Step 2: Import with specific dtypes
dtypes = {
    'Column11': 'bool',  # Adjust column names as needed
    'Column12': 'str',
    # Add other columns with specific dtypes
}

data = pd.read_csv('leads.csv', dtype=dtypes)
