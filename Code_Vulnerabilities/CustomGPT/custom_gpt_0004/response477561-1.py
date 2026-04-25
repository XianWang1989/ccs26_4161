
import pandas as pd
from datetime import datetime

startTime = datetime.now()

# Define the path to your CSV file
data_path = r"C:\Users\eduardo\.xy\startups\INDV14.CSV"

# Use pandas to read the CSV file with specified delimiters
df = pd.read_csv(data_path, sep='[; ]', engine='python', header=None)

# Extract the third column (index 2)
ticks = df[2].astype(int)  # Convert to integers directly

# Create a DataFrame and compute pct_change
deals = pd.DataFrame(ticks)
daily_returns = deals.pct_change(periods=1)

# Save the daily returns to a new CSV file
daily_returns.to_csv('returns.csv', index=False)

print(daily_returns)
print("Time taken:", datetime.now() - startTime)
