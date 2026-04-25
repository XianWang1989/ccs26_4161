
import pandas as pd
from datetime import datetime

startTime = datetime.now()

# Define file path
data_path = "C:\\Users\\eduardo\\.xy\\startups\\INDV14.CSV"

# Read the CSV file directly into a DataFrame
df = pd.read_csv(data_path, sep='[ ;]', header=None, engine='python')

# Extract the third column (index 2) into a new DataFrame
ticks = df[2].astype(int)  # Convert to integers

# Calculate percentage change
daily_returns = ticks.pct_change(periods=1)

# Print daily returns
print(daily_returns)

# Save the results to a new CSV file
daily_returns.to_csv('returns.csv', index=False)

# Time taken
print("Time taken:", datetime.now() - startTime)
