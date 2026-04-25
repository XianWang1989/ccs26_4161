
import pandas as pd

# Specify the columns of concern with their intended type as string
cols_of_interest = ['Column11', 'Column12', 'Column13', 'Column14', 'Column17', 'Column19', 'Column20', 'Column21']

# Read the CSV file while treating specific columns as strings
data = pd.read_csv('leads.csv', dtype={col: str for col in cols_of_interest}, low_memory=False)

# Now you can apply checks to find issues.
# Example: Identifying non-boolean values in Column K (Column11)
boolean_values = {'TRUE', 'FALSE', ''}  # Include empty strings if that is valid.
invalid_rows = data[~data['Column11'].isin(boolean_values)]

# Display rows with invalid entries
print(invalid_rows)
