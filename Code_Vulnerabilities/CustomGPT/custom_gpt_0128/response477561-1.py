
import pandas as pd
from datetime import datetime

startTime = datetime.now()

# Define the path to your CSV file
data_path = r"C:\Users\eduardo\.xy\startups\INDV14.CSV"

# Read the CSV file, specifying the delimiter
df = pd.read_csv(data_path, delimiter=';', header=None, usecols=[2], names=['ticks'])

# Convert the ticks column to integers
df['ticks'] = df['ticks'].astype(int)

# Calculate the daily returns using pct_change
daily_returns = df['ticks'].pct_change(periods=1)

# Save the results to a new CSV file
daily_returns.to_csv('returns.csv', index=False)

print(f"Processing time: {datetime.now() - startTime}")
