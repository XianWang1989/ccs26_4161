
import pandas as pd
from datetime import datetime

startTime = datetime.now()

data = "C:\\Users\\eduardo\\.xy\\startups\\INDV14.CSV"

# Read the CSV directly into a DataFrame
df = pd.read_csv(data, sep=';', header=None, names=['Date', 'Time', 'Value'], engine='python')

# Extract the third column and convert to numeric
df['Value'] = pd.to_numeric(df['Value'], errors='coerce')

# Calculate the percentage change
daily_returns = df['Value'].pct_change(periods=1)

# Save the results to a new CSV file
daily_returns.to_csv('returns.csv', index=False)

print(daily_returns)

print("Processing Time:", datetime.now() - startTime)
