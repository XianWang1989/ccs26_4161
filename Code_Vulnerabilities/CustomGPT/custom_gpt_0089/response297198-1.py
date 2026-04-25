
import pandas as pd

# Load the CSV file with all data as strings
data = pd.read_csv('leads.csv', dtype=str)

# Check for inconsistencies in the problematic columns
# Replace 'column_k' with the relevant column name
problematic_column = 'column_k'  # Change to the actual column name
inconsistencies = data[~data[problematic_column].isin(['TRUE', 'FALSE'])]

print("Rows with inconsistencies in column K:")
print(inconsistencies)
