
import pandas as pd
from datetime import datetime

start_time = datetime.now()

# Path to your CSV file
data_path = r"C:\Users\eduardo\.xy\startups\INDV14.CSV"

# Read the CSV file with proper delimiter
df = pd.read_csv(data_path, delimiter=';', header=None, names=['DateTime', 'Value1', 'Close'])

# Extract the 'Close' column
close_prices = df['Close']

# Compute the percentage change
daily_returns = close_prices.pct_change(periods=1)

# Save the results to a new CSV file
daily_returns.to_csv('returns.csv', index=False)

# Print elapsed time
print(datetime.now() - start_time)
