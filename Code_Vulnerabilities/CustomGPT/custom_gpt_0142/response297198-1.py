
import pandas as pd

# Load the CSV with specific columns as string to avoid dtype warnings
df = pd.read_csv('leads.csv', usecols=[11, 12, 13, 14, 17, 19, 20, 21], dtype=str)

# Check for any rows that are not consistent with expected types
# For example, for column 11 which is supposed to be Boolean
bool_issues = df[~df[11].isin(['TRUE', 'FALSE'])]

# Display the problematic rows
print("Rows with issues in Column 11:")
print(bool_issues)
