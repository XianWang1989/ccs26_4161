
import pandas as pd

# Define the columns to check for mixed types
columns_to_check = [11, 12, 13, 14, 17, 19, 20, 21]  # 0-indexed columns

# Initialize a list to store problematic rows
problematic_rows = []

# Read the CSV in chunks and check data types
for chunk in pd.read_csv('leads.csv', chunksize=1000):
    for col in columns_to_check:
        if chunk.iloc[:, col].dtype == 'object':
            # Check for values that are not consistent
            inconsistent_values = chunk.iloc[:, col].unique()
            if len(inconsistent_values) > 2:  # Adjust as needed
                problematic_rows.append(chunk[chunk.iloc[:, col].isin(inconsistent_values)])

# Display problematic rows
for index, rows in enumerate(problematic_rows):
    print(f"Problematic Rows from chunk {index}:")
    print(rows)
