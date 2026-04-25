
import pandas as pd
from datetime import datetime

start_time = datetime.now()

# Define the file path
data_path = r"C:\Users\eduardo\.xy\startups\INDV14.CSV"

# Read the CSV file directly into a DataFrame
# Specify the delimiter based on your CSV format
df = pd.read_csv(data_path, delimiter=';', header=None)

# Extract the third column (index 2)
ticks = df[2]

# Calculate percentage change
daily_returns = ticks.pct_change()

# Save the results to a new CSV file
daily_returns.to_csv('returns.csv', index=False)

print("Execution time:", datetime.now() - start_time)
