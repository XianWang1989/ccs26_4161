
import pandas as pd
from datetime import datetime

startTime = datetime.now()

# Path to your CSV data
data_path = r"C:\Users\eduardo\.xy\startups\INDV14.CSV"

# Read the CSV directly into a DataFrame
df = pd.read_csv(data_path, sep=';', usecols=[2], header=None)

# Convert the third column to integers
df[0] = df[0].astype(int)

# Calculate the percentage change
daily_returns = df[0].pct_change()

# Save the results to a new CSV file
daily_returns.to_csv('returns.csv', index=False, header=False)

print(daily_returns)
print("Execution time:", datetime.now() - startTime)
