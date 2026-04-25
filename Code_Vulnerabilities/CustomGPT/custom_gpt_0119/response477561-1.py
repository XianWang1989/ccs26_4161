
import pandas as pd
from datetime import datetime

startTime = datetime.now()

# Define the path to your CSV file
data = r"C:\Users\eduardo\.xy\startups\INDV14.CSV"

# Read the CSV file using pandas
# Assuming the delimiter is a semicolon and space
df = pd.read_csv(data, sep='[ ;]', engine='python', header=None)

# Extract the third column (index 2)
ticks = df[2]

# Convert to integer type
ticks = ticks.astype(int)

# Create a DataFrame and compute pct_change
deals = pd.DataFrame(ticks)
daily_returns = deals.pct_change(periods=1)

# Save results to a new CSV file
daily_returns.to_csv('returns.csv', index=False)

print(daily_returns)
print("Processing time:", datetime.now() - startTime)
