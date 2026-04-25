
import pandas as pd
from datetime import datetime

# Start timer
start_time = datetime.now()

# File paths
data_path = r"C:\Users\eduardo\.xy\startups\INDV14.CSV"

# Read the CSV file using pandas
# Specify the delimiter based on your data format
df = pd.read_csv(data_path, sep='[; ]', header=None, engine='python')

# Extract the third column (index 2)
ticks = df[2].astype(int)

# Calculate percentage change
daily_returns = ticks.pct_change()

# Save results to a new CSV file
daily_returns.to_csv('returns.csv', index=False)

# Print elapsed time
print(datetime.now() - start_time)
