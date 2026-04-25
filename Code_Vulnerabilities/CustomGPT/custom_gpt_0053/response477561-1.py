
import pandas as pd
import time

# Start timing
startTime = time.time()

# Path to the CSV file
data_path = "C:\\Users\\eduardo\\.xy\\startups\\INDV14.CSV"

# Read the CSV file
# Adjusting the separator to handle your given format
df = pd.read_csv(data_path, sep=';', header=None)

# Extract the third column (index 2)
ticks = df[2]

# Convert ticks to numeric type
ticks = pd.to_numeric(ticks, errors='coerce')

# Calculate pct_change
daily_returns = ticks.pct_change()

# Save the results to a new CSV file
daily_returns.to_csv('returns.csv', index=False)

# Print the execution time
print(f"Execution Time: {time.time() - startTime} seconds")
