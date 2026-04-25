
import pandas as pd
from datetime import datetime

start_time = datetime.now()

# Define the path to the CSV file
data_path = r"C:\Users\eduardo\.xy\startups\INDV14.CSV"

# Read the CSV file directly using pandas
# Use the appropriate delimiter based on your data
df = pd.read_csv(data_path, delimiter=';', header=None)

# Extract the third column (index 2)
ticks = df[2]

# Calculate the percentage change
daily_returns = ticks.pct_change(periods=1)

# Save the results to a new CSV file
daily_returns.to_csv('returns.csv', index=False)

print(daily_returns)
print("Time taken:", datetime.now() - start_time)
