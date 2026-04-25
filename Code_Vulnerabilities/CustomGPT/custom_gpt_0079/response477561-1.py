
import pandas as pd
from datetime import datetime

startTime = datetime.now()

# Define the path to your CSV file
file_path = "C:\\Users\\eduardo\\.xy\\startups\\INDV14.CSV"

# Read the CSV file using pandas
data = pd.read_csv(file_path, delimiter=';', header=None)

# Extract the third column (index 2)
ticks = data[2]

# Convert ticks to integers
ticks = ticks.astype(int)

# Calculate daily returns using pct_change
daily_returns = ticks.pct_change()

# Save the results to CSV
daily_returns.to_csv('returns.csv', index=False)

print("Processing time:", datetime.now() - startTime)
