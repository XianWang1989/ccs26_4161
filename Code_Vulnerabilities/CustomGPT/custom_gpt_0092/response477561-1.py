
import pandas as pd
from datetime import datetime

# Start the timer
startTime = datetime.now()

# File path
data_path = r"C:\Users\eduardo\.xy\startups\INDV14.CSV"

# Read the CSV using pandas with specified delimiters
# This assumes semicolon as the main delimiter between columns
df = pd.read_csv(data_path, delimiter=';', header=None)

# Extract the third column (index 2)
ticks = df[2].astype(int)  # Convert to integers

# Create DataFrame and compute percentage change
deals = pd.DataFrame(ticks)
daily_returns = deals.pct_change(periods=1)

# Save daily returns to a new CSV file
daily_returns.to_csv('returns.csv', index=False)

# Print elapsed time
print("Time taken:", datetime.now() - startTime)
