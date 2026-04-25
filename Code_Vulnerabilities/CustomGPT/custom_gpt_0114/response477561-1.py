
import pandas as pd
from datetime import datetime

startTime = datetime.now()

# Specify the path to your CSV file
data_path = "C:\\Users\\eduardo\\.xy\\startups\\INDV14.CSV"

# Use pandas to read the CSV file with appropriate delimiters
df = pd.read_csv(data_path, delimiter=';', header=None)

# Select the third column (index 2)
ticks = df[2]

# Compute the percentage change
daily_returns = ticks.pct_change(periods=1)

# Output to CSV
daily_returns.to_csv('returns.csv', index=False, header=False)

print(daily_returns)
print(f"Time taken: {datetime.now() - startTime}")
