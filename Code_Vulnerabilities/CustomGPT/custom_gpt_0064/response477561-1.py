
import pandas as pd
from datetime import datetime

startTime = datetime.now()

# Define the file path
data_path = "C:\\Users\\eduardo\\.xy\\startups\\INDV14.CSV"

# Read the CSV file into a DataFrame
# Use the correct delimiter based on your data format
df = pd.read_csv(data_path, delim_whitespace=True, header=None)

# Select the third column (index 2)
ticks = df[2]

# Convert the ticks to integers (if necessary)
ticks = ticks.astype(int)

# Create a DataFrame for pct_change calculation
deals = pd.DataFrame(ticks)

# Calculate percentage change
daily_returns = deals.pct_change(periods=1)

# Output the results
print(daily_returns)

# Save the output to a CSV file
daily_returns.to_csv('returns.csv', index=False)

print("Execution time:", datetime.now() - startTime)
