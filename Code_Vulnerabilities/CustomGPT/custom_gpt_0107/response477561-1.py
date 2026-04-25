
import pandas as pd
from datetime import datetime

# Start time for performance measurement
startTime = datetime.now()

# Define the path to your CSV file
data_path = "C:\\Users\\eduardo\\.xy\\startups\\INDV14.CSV"

# Read the CSV file, specifying the delimiter
# Use 'sep' for delimiter; assume ';' as the column separator
# Adjust header if necessary
df = pd.read_csv(data_path, sep=';', header=None)

# Extract the third column (index 2)
ticks = df[2]

# Convert to numeric, errors='coerce' converts non-numeric values to NaN
ticks = pd.to_numeric(ticks, errors='coerce')

# Calculate percent change
daily_returns = ticks.pct_change(periods=1)

# Save to a new CSV file
daily_returns.to_csv('returns.csv', index=False)

# Output execution time
print("Execution Time:", datetime.now() - startTime)
