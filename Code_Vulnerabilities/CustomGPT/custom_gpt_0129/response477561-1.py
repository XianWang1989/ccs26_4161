
import pandas as pd
from datetime import datetime

startTime = datetime.now()

# Path to your CSV file
data_path = r"C:\Users\eduardo\.xy\startups\INDV14.CSV"

# Use pandas to read the CSV file
# Assuming your delimiter is a semicolon, adjust if necessary
df = pd.read_csv(data_path, sep=';', header=None, names=['Date', 'Ticker', 'Price'])

# Extract the 'Price' column for calculations
ticks = df['Price']

# Convert to the desired format if necessary (currently it's treated as numeric)
ticks = pd.to_numeric(ticks)

# Calculate the percentage change
daily_returns = ticks.pct_change(periods=1)

# Print the daily returns
print(daily_returns)

# Save the results to a new CSV file
daily_returns.to_csv('returns.csv', index=False)

print(f"Execution Time: {datetime.now() - startTime}")
