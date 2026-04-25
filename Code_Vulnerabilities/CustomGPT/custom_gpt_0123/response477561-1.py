
import pandas as pd
from datetime import datetime

# Start time for performance measurement
startTime = datetime.now()

# Define file path
data_path = "C:\\Users\\eduardo\\.xy\\startups\\INDV14.CSV"

# Read the CSV with appropriate delimiters
# You can use a regex for split on both space and semicolon
data = pd.read_csv(data_path, delimiter='[ ;]+', header=None)

# Extract the third column (index 2)
ticks = data.iloc[:, 2]

# Compute the percent change
daily_returns = ticks.pct_change()

# Save to a new CSV file
daily_returns.to_csv('returns.csv', index=False)

# Print the execution time
print(f"Execution time: {datetime.now() - startTime}")
