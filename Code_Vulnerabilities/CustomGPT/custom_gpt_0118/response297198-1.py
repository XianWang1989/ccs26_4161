
import pandas as pd

# Initialize a list to store rows with problems
problematic_rows = []

# Read the CSV in chunks
for chunk in pd.read_csv('leads.csv', chunksize=1000):
    for index, row in chunk.iterrows():
        # Check for data types in the specific columns
        if not all(isinstance(row[col], (str, bool)) for col in [11, 12, 13, 14, 17, 19, 20, 21]):
            problematic_rows.append(row)

# Convert to a DataFrame for easier analysis
problematic_df = pd.DataFrame(problematic_rows)
print(problematic_df)
