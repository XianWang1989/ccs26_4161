
import pandas as pd
from datetime import datetime

startTime = datetime.now()

# Set the path to your CSV file
data_path = "C:\\Users\\eduardo\\.xy\\startups\\INDV14.CSV"

# Read the CSV file directly using pandas
# Specify the delimiter as it looks like your data is semi-colon separated
# and has spaces in the first column which you may want to skip
df = pd.read_csv(data_path, sep=';', header=None)

# Extract the third column (index 2)
close_prices = df[2]

# Convert it to numeric (this will handle strings that are not convertible to numbers)
close_prices = pd.to_numeric(close_prices, errors='coerce')

# Calculate the percent change
daily_returns = close_prices.pct_change(periods=1)

# Write the result to a new CSV file
daily_returns.to_csv('returns.csv', index=False, header=False)

# Output the elapsed time
print("Elapsed time:", datetime.now() - startTime)
