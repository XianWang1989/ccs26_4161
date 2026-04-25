
import pandas as pd
from datetime import datetime

startTime = datetime.now()

# Define the path to the CSV file
data_path = r"C:\Users\eduardo\.xy\startups\INDV14.CSV"

# Read the CSV file directly using pandas, specifying the delimiter
df = pd.read_csv(data_path, delimiter='[; ]', engine='python', header=None)

# Extract the third column (index 2)
ticks = df[2].astype(int)  # Convert to integer

# Calculate pct_change
daily_returns = ticks.pct_change(periods=1)

# Save the results to a new CSV file
daily_returns.to_csv('returns.csv', index=False)

print(daily_returns)
print("Processing time:", datetime.now() - startTime)
