
import pandas as pd
from datetime import datetime

startTime = datetime.now()

# Define the path to your CSV file
data_path = "C:\\Users\\eduardo\\.xy\\startups\\INDV14.CSV"

# Read the CSV file with specified delimiter
# Since your CSV uses a semicolon, we will specify that
df = pd.read_csv(data_path, delimiter=';', header=None)

# Extract the third column, which is index 2 (zero-based index)
ticks = df[2]  # Third column as a Series

# Convert to numeric (if needed), and drop any non-numeric values
ticks = pd.to_numeric(ticks, errors='coerce').dropna()

# Compute the percentage change
daily_returns = ticks.pct_change()

# Print or save daily returns
print(daily_returns)

# Save to CSV
daily_returns.to_csv('returns.csv', index=False)

print("Time taken:", datetime.now() - startTime)
