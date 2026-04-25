
import pandas as pd

# Initialize an empty DataFrame to store problem rows
problem_rows = pd.DataFrame()

# Iterate through the file in chunks
chunk_size = 1000  # Adjust as necessary
for chunk in pd.read_csv('leads.csv', chunksize=chunk_size):
    # Check for rows with mixed types in specific columns
    for column in [11, 12, 13, 14, 17, 19, 20, 21]:  # Indices of problem columns
        mixed_type_rows = chunk[chunk[column].apply(type).ne(chunk[column].iloc[0].apply(type))]
        problem_rows = pd.concat([problem_rows, mixed_type_rows])

# Display the problem rows
print(problem_rows)
