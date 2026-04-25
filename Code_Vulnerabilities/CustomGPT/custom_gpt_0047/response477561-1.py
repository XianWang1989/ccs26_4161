
import pandas as pd
from datetime import datetime

startTime = datetime.now()

# Define the path to your CSV file
data_file = r"C:\Users\eduardo\.xy\startups\INDV14.CSV"

# Read the CSV file directly using pandas
df = pd.read_csv(data_file, sep=';', header=None)

# Extract the third column (index 2)
ticks = df[2].astype(int)

# Calculate the percent change
daily_returns = ticks.pct_change()

# Print the daily returns
print(daily_returns)

# Save the results to a new CSV file
daily_returns.to_csv('returns.csv', index=False)

# Print the time taken for execution
print("Time taken:", datetime.now() - startTime)
