
import pandas as pd
from datetime import datetime

# Start time for performance tracking
startTime = datetime.now()

# Define the path to your CSV file
data_path = "C:\\Users\\eduardo\\.xy\\startups\\INDV14.CSV"

# Load the CSV file into a DataFrame
# Specify the separator to handle your data format
df = pd.read_csv(data_path, sep=';', usecols=[2], names=['ticks'], header=None)

# Convert the ticks column to numeric, if needed
df['ticks'] = pd.to_numeric(df['ticks'])

# Calculate the percentage change
daily_returns = df['ticks'].pct_change()

# Save the daily returns to a new CSV file
daily_returns.to_csv('returns.csv', index=False)

# Print the computation time
print("Time taken:", datetime.now() - startTime)

# Optional: print daily returns
print(daily_returns)
