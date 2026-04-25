
import pandas as pd
from datetime import datetime

start_time = datetime.now()

# Path to your CSV file
data_path = "C:\\Users\\eduardo\\.xy\\startups\\INDV14.CSV"

# Read the CSV file using pandas
# Specify 'delimiter' to handle your specific format
df = pd.read_csv(data_path, delimiter=';', header=None, usecols=[2], names=['ticks'])

# Calculate the percentage change
daily_returns = df['ticks'].astype(int).pct_change(periods=1)

# Save the results to a new CSV file
daily_returns.to_csv('returns.csv', index=False)

print(daily_returns)

# Time elapsed
print("Time elapsed:", datetime.now() - start_time)
