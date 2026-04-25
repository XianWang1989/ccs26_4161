
import pandas as pd
from datetime import datetime

startTime = datetime.now()

# File paths
data = r"C:\Users\eduardo\.xy\startups\INDV14.CSV"
output_csv = 'returns.csv'

# Read the CSV file using pandas
df = pd.read_csv(data, sep='[; ]', header=None, engine='python')

# Extract the third column (index 2)
ticks = df[2].astype(int)  # Convert to int directly

# Calculate pct_change
daily_returns = ticks.pct_change(periods=1)

# Save the returns to a new CSV file
daily_returns.to_csv(output_csv, index=False)

# Print execution time
print("Time taken:", datetime.now() - startTime)
