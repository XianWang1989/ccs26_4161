
import pandas as pd
from datetime import datetime

startTime = datetime.now()

# Define the file path
data_path = "C:\\Users\\eduardo\\.xy\\startups\\INDV14.CSV"

# Read the CSV file directly using pandas
# Use the `sep` option to specify the delimiter
df = pd.read_csv(data_path, sep='[; ]+', engine='python', header=None)

# Extract the third column (index 2)
ticks = df[2]

# Convert to numeric (if necessary)
ticks = pd.to_numeric(ticks, errors='coerce')

# Calculate percentage change
daily_returns = ticks.pct_change(periods=1)

# Save to a new CSV file
daily_returns.to_csv('returns.csv', index=False)

print(f"Processing time: {datetime.now() - startTime}")
