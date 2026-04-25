
import pandas as pd
from datetime import datetime

startTime = datetime.now()

# Specify the path to your CSV file
data_path = r"C:\Users\eduardo\.xy\startups\INDV14.CSV"

# Read the CSV file into a DataFrame
# Use the correct delimiter
df = pd.read_csv(data_path, delimiter=';', header=None)

# Extract the third column (index 2)
ticks = df[2]

# Convert to numeric (if not already)
ticks = pd.to_numeric(ticks, errors='coerce')

# Calculate percentage change
daily_returns = ticks.pct_change(periods=1)

# Save to a new CSV file
daily_returns.to_csv('returns.csv', index=False)

print(daily_returns)
print("Processing time:", datetime.now() - startTime)
