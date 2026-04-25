
import pandas as pd

# Read the CSV file with error_bad_lines to skip problematic rows
df = pd.read_csv('leads.csv', error_bad_lines=False)

# Check the data types of each column
print(df.dtypes)

# Identify problematic rows
for column in ['Column11', 'Column12', 'Column13', 'Column14', 'Column17', 'Column19', 'Column20', 'Column21']:
    # Attempt to convert to a specific type/format and coerce errors
    result = pd.to_numeric(df[column], errors='coerce')
    # Print the rows which couldn't be converted
    print(f"Rows with issues in {column}:\n", df[result.isna()].index.tolist())
