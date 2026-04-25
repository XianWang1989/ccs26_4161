
import pandas as pd
from datetime import datetime

startTime = datetime.now()

# Path to your CSV file
data_path = "C:\\Users\\eduardo\\.xy\\startups\\INDV14.CSV"

# Read the CSV directly into a DataFrame
# Set appropriate delimiter
df = pd.read_csv(data_path, delimiter=';', usecols=[2], header=None)

# Calculate percentage change
daily_returns = df.pct_change()

# Save to new CSV file
daily_returns.to_csv('returns.csv', index=False)

print(daily_returns)
print(f"Processing time: {datetime.now() - startTime}")
