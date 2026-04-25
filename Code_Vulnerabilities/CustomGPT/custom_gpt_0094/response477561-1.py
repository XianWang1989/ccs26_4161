
import pandas as pd
from datetime import datetime

startTime = datetime.now()

# Define the path to your CSV file
data_path = "C:\\Users\\eduardo\\.xy\\startups\\INDV14.CSV"

# Read the CSV file, specifying the delimiter
df = pd.read_csv(data_path, delimiter=';', header=None, usecols=[2], names=['ticks'])

# Calculate the percentage change
daily_returns = df['ticks'].pct_change()

# Save to a new CSV file
daily_returns.to_csv('returns.csv', header=False, index=False)

print(daily_returns)
print("Processing time:", datetime.now() - startTime)
