
import pandas as pd
from datetime import datetime

startTime = datetime.now()

data = "C:\\Users\\eduardo\\.xy\\startups\\INDV14.CSV"

# Using pandas to read the csv file
# Specify the correct delimiter, assuming the second column is separated by a semicolon
df = pd.read_csv(data, sep=';', header=None)

# Extracting the third column where column index is 2
ticks = df[2]

# Convert to numeric (if needed) and compute percentage change
ticks = pd.to_numeric(ticks, errors='coerce')  # Convert to numeric and handle errors
daily_returns = ticks.pct_change(periods=1)

# Saving the result to a new CSV file
daily_returns.to_csv('returns.csv', index=False)

# Print the runtime
print("Time taken:", datetime.now() - startTime)
