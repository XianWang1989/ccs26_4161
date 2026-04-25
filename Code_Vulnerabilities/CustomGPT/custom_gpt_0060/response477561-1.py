
import pandas as pd
from datetime import datetime

# Start time to measure performance
startTime = datetime.now()

# Path to the CSV file
data_path = "C:\\Users\\eduardo\\.xy\\startups\\INDV14.CSV"

# Read the CSV file directly into a DataFrame
# Specify the separator used in the CSV (in your case, it seems to use both space and semicolon)
df = pd.read_csv(data_path, sep='[ ;]+', header=None, engine='python')

# Extract the third column (index 2)
ticks = df[2]

# Convert ticks to numeric if they are not already
ticks = pd.to_numeric(ticks, errors='coerce')

# Create a DataFrame for ticks
deals = pd.DataFrame(ticks)

# Calculate the percentage change
daily_returns = deals.pct_change(periods=1)

# Print daily returns (or you can save it to a CSV)
print(daily_returns)

# Save to CSV
daily_returns.to_csv('returns.csv', index=False)

# Measure total execution time
elapsed_time = datetime.now() - startTime
print(f"Elapsed Time: {elapsed_time}")
