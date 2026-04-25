
import pandas as pd
from datetime import datetime

startTime = datetime.now()

# Specify the CSV file path
data = "C:\\Users\\eduardo\\.xy\\startups\\INDV14.CSV"

# Read the CSV file using pandas
# Adjusting the delimiter to match the provided format
df = pd.read_csv(data, delimiter=';', header=None)

# Extract the third column directly
ticks = df[2].astype(int)

# Create DataFrame and compute pct_change
deals = pd.DataFrame(ticks)
daily_returns = deals.pct_change(periods=1)

# Output the result
print(daily_returns)

# Save the returns to a new CSV file
daily_returns.to_csv('returns.csv', index=False, header=False)

print(datetime.now() - startTime)  # Time counter
