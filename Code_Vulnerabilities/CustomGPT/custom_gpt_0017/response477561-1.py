
import pandas as pd
from datetime import datetime

startTime = datetime.now()

# Define file path
data = r"C:\Users\eduardo\.xy\startups\INDV14.CSV"

# Read the CSV file directly into a DataFrame
# Use the appropriate delimiter and specify column names
df = pd.read_csv(data, delimiter=';', header=None, usecols=[2], names=['ticks'])

# Convert the ticks column to integers
df['ticks'] = df['ticks'].astype(int)

# Calculate percentage change
daily_returns = df['ticks'].pct_change()

# Save the results to a new CSV file
daily_returns.to_csv('returns.csv', index=False)

print(daily_returns)
print("Processing time: ", datetime.now() - startTime)
