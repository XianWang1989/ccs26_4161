
import pandas as pd
from datetime import datetime

startTime = datetime.now()

# Path to your CSV file
data = "C:\\Users\\eduardo\\.xy\\startups\\INDV14.CSV"

# Read the CSV file using pandas
# Use the correct delimiter for your CSV format (in this case, `;`)
df = pd.read_csv(data, delimiter=';', header=None)

# Select the third column (which corresponds to index 2)
ticks = df[2].astype(int)  # Convert to integers

# Calculate pct_change
daily_returns = ticks.pct_change(periods=1)

# Save results to a new CSV file
daily_returns.to_csv('returns.csv', index=False)

print(daily_returns)
print("Time taken:", datetime.now() - startTime)
