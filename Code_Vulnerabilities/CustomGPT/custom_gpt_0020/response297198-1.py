
import pandas as pd

# Load the CSV file with all columns as strings
leads = pd.read_csv('leads.csv', dtype=str)

# Check specific columns for mixed types (Column K = index 10)
problematic_rows = leads[leads[leads.columns[10]].isin(['TRUE', 'FALSE']) == False]

# Display rows that have mixed types
print("Problematic Rows:")
print(problematic_rows)
