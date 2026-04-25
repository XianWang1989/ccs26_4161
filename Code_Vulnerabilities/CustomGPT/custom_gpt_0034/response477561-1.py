
import pandas as pd
from datetime import datetime

startTime = datetime.now()

# Define the file path
data_path = "C:\\Users\\eduardo\\.xy\\startups\\INDV14.CSV"

# Read the CSV file using pandas
# Use the correct delimiter and ensure no unnecessary processing
df = pd.read_csv(data_path, sep=';', header=None, usecols=[2], names=['ticks'])

# Convert the ticks to integers
df['ticks'] = df['ticks'].astype(int)

# Calculate percent change
daily_returns = df['ticks'].pct_change(periods=1)

# Print the daily returns
print(daily_returns)

# Save to a new CSV file
daily_returns.to_csv('returns.csv', index=False)

# Display elapsed time
print("Elapsed time:", datetime.now() - startTime)
