
import pandas as pd
from datetime import datetime

startTime = datetime.now()

# Path to the CSV file
data_path = r"C:\Users\eduardo\.xy\startups\INDV14.CSV"

# Read the CSV file directly with pandas
# Specify the delimiter and the columns to read
df = pd.read_csv(data_path, delimiter=';', usecols=[1, 2], header=None)

# Extract the third column (adjust index if needed)
ticks = df[2].astype(int)

# Calculate the percentage change
daily_returns = ticks.pct_change()

# Print the daily returns
print(daily_returns)

# Save the results to a new CSV file
daily_returns.to_csv('returns.csv', index=False, header=False)

# Print elapsed time
print("Elapsed time:", datetime.now() - startTime)
