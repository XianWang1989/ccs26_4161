
import pandas as pd
from datetime import datetime

# Start time for performance tracking
start_time = datetime.now()

# File path
data_path = r"C:\Users\eduardo\.xy\startups\INDV14.CSV"

# Load the CSV file directly into a DataFrame
# Use the correct delimiter based on the example provided
df = pd.read_csv(data_path, delimiter=';', header=None)

# Extract the third column (index 2)
ticks = df[2]

# Convert to numeric, forcing errors to NaN
ticks = pd.to_numeric(ticks, errors='coerce')

# Calculate the percentage change
daily_returns = ticks.pct_change(periods=1)

# Save to new CSV file
daily_returns.to_csv('returns.csv', index=False)

# Stop time and print duration
print(f"Processing time: {datetime.now() - start_time}")
