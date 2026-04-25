
import pandas as pd
from datetime import datetime

# Start timing
startTime = datetime.now()

# Define the path to the CSV file
data_path = r"C:\Users\eduardo\.xy\startups\INDV14.CSV"

# Read the CSV file directly into a DataFrame
# Specify the separator
df = pd.read_csv(data_path, sep=';', header=None, usecols=[2])

# Convert the third column to a numeric type (int or float)
df[2] = pd.to_numeric(df[2], errors='coerce')

# Calculate the percentage change
daily_returns = df[2].pct_change()

# Write the results to a new CSV file
daily_returns.to_csv('returns.csv', index=False)

# Print execution time
print("Execution time:", datetime.now() - startTime)
