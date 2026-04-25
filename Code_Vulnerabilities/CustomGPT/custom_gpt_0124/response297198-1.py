
import pandas as pd

# Define the columns to check for mixed types
columns_to_check = ['ColumnK', 'Column12', 'Column13', 'Column14', 'Column17', 'Column19', 'Column20', 'Column21']

# Read the CSV in chunks
chunk_iterator = pd.read_csv('leads.csv', chunksize=1000)

# Initialize a list to store problematic rows
bad_rows = []

for chunk in chunk_iterator:
    for column in columns_to_check:
        # Check for non-boolean types in ColumnK, or non-string types in others
        if not pd.api.types.is_bool_dtype(chunk[column]) and column == 'ColumnK':
            bad_rows.append(chunk[chunk[column].apply(lambda x: type(x) != bool)])
        elif not pd.api.types.is_string_dtype(chunk[column]):
            bad_rows.append(chunk[chunk[column].apply(lambda x: not isinstance(x, str))])

# Combine all bad rows into a single DataFrame
bad_rows_df = pd.concat(bad_rows, ignore_index=True)
print(bad_rows_df)
