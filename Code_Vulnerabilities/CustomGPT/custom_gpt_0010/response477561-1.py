
import pandas as pd
from datetime import datetime

startTime = datetime.now()

# Path to your CSV file
data_path = "C:\\Users\\eduardo\\.xy\\startups\\INDV14.CSV"

# Read the CSV file with proper delimiters
# Assuming your data is separated first by space and then by semicolon
df = pd.read_csv(data_path, delimiter='[; ]', engine='python', header=None)

# Extract the third column (index 2)
ticks = df[2]

# Compute percentage change
daily_returns = ticks.pct_change()

# Print daily returns
print(daily_returns)

# Save the results to a new CSV file
daily_returns.to_csv('returns.csv', index=False)

# Time taken
print("Time taken:", datetime.now() - startTime)
