
import pandas as pd

# Load the CSV with specified dtypes
dtypes = {
    'Column11': 'object',  # Change to object for mixed types
    'Column12': 'object',  # Do the same for others as needed
    # Specify other columns here as well...
}

# Read the CSV with low_memory=False to load it in one go
data = pd.read_csv('leads.csv', dtype=dtypes, low_memory=False)

# Optional: Find rows in the problematic columns where data is inconsistent
for col in ['Column11', 'Column12']:  # Add other columns as needed
    inconsistent_rows = data[~data[col].isin(['TRUE', 'FALSE'])]  # Adjust for specific data
    print(f"Inconsistent rows in {col}:\n", inconsistent_rows)
