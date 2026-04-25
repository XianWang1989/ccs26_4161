
import pandas as pd

# Define specific dtypes for problematic columns
dtypes = {
    'ColumnNameK': 'bool',  # Replace with actual column names
    # Define other columns as necessary
    'ColumnNameN': 'category',  # For strings with limited unique values
    # Add remaining columns
}

# Read the CSV while specifying dtypes and low_memory
data = pd.read_csv('leads.csv', dtype=dtypes, low_memory=False)

# Print a sample of the data
print(data.head())
