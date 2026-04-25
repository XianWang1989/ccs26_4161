
import pandas as pd

# Load the data with error handling
data = pd.read_csv('leads.csv', error_bad_lines=False)  # This skips bad lines

# Inspect the specific columns to look for inconsistencies
cols_to_check = [11, 12, 13, 14, 17, 19, 20, 21]
for col in cols_to_check:
    # Display unique values in the column to identify issues
    print(f"Column {col} unique values:")
    print(data.iloc[:, col].unique())
