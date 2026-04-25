
import pandas as pd
from datetime import datetime

startTime = datetime.now()

# Define the path to your CSV file
data_path = "C:\\Users\\eduardo\\.xy\\startups\\INDV14.CSV"

# Using Pandas to read the CSV file directly
# You can specify the delimiters here
# Since you have a mixed delimiter (space and semicolon), we can use regex
df = pd.read_csv(data_path, sep=r'[ ;]', header=None)

# Extract the third column (index 2)
ticks = df[2].astype(int)  # Convert to integers directly with astype

# Calculate the percentage change
daily_returns = ticks.pct_change(periods=1)

# Print the daily returns
print(daily_returns)

# Write the results to a new CSV file
daily_returns.to_csv('returns.csv', index=False)

# Output the elapsed time
elapsed_time = datetime.now() - startTime
print(f"Elapsed time: {elapsed_time}")
