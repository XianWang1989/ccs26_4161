
import pandas as pd
import time

start_time = time.time()

# File path
data_path = "C:\\Users\\eduardo\\.xy\\startups\\INDV14.CSV"

# Load the CSV using pandas, specifying the delimiter
# Use `header=None` if there are no headers in your CSV
df = pd.read_csv(data_path, sep=';', header=None)

# Extract the third column (index 2)
ticks = df[2]

# Convert the ticks to integers
ticks = ticks.astype(int)

# Create a DataFrame
deals = pd.DataFrame(ticks)

# Calculate the percentage change
daily_returns = deals.pct_change(periods=1)

# Save to CSV
daily_returns.to_csv('returns.csv', index=False)

print(f"Processing time: {time.time() - start_time:.2f} seconds")
