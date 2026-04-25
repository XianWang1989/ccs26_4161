
import pandas as pd
from datetime import datetime

startTime = datetime.now()

# Path to the CSV file
data_path = "C:\\Users\\eduardo\\.xy\\startups\\INDV14.CSV"

# Read the CSV file using pandas
# Use semicolon as a delimiter and specify the names of columns
data = pd.read_csv(data_path, sep=';', header=None, usecols=[2], names=['close'])

# Calculate the percentage change
daily_returns = data['close'].pct_change()

# Save the daily returns to a new CSV file
daily_returns.to_csv('returns.csv', index=False)

print(daily_returns)
print("Processing time:", datetime.now() - startTime)
