
import pandas as pd
from datetime import datetime

startTime = datetime.now()

# Path to the CSV file
data_path = r"C:\Users\eduardo\.xy\startups\INDV14.CSV"

# Read the CSV file into a DataFrame
# Use `delimiter` to specify separators
df = pd.read_csv(data_path, delimiter=';', header=None, usecols=[2], names=['ticks'])

# Convert the ticks column to numeric
df['ticks'] = pd.to_numeric(df['ticks'], errors='coerce')

# Calculate percentage change
daily_returns = df['ticks'].pct_change()

# Save the results to a new CSV file
daily_returns.to_csv('returns.csv', index=False)

print(daily_returns)
print("Time taken:", datetime.now() - startTime)
