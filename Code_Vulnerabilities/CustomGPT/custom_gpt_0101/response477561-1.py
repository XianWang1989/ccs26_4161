
import pandas as pd
from datetime import datetime

startTime = datetime.now()

data_path = "C:\\Users\\eduardo\\.xy\\startups\\INDV14.CSV"

# Read CSV directly into a DataFrame
df = pd.read_csv(data_path, delimiter=';', usecols=[2], header=None)

# Calculate pct_change directly
daily_returns = df.pct_change(periods=1)

# Save to CSV
daily_returns.to_csv('returns.csv', index=False)

print("Processing time:", datetime.now() - startTime)
