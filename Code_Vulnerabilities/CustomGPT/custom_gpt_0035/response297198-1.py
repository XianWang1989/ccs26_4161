
import pandas as pd

# Define the columns you suspect may have mixed types
problematic_columns = [11, 12, 13, 14, 17, 19, 20, 21]  # Index if needed
chunk_size = 1000

# Read the CSV in chunks
for chunk in pd.read_csv('leads.csv', chunksize=chunk_size):
    for col in problematic_columns:
        print(chunk.iloc[:, col].apply(type).value_counts())
