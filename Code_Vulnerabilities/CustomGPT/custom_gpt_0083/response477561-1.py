
import pandas as pd
from datetime import datetime

startTime = datetime.now()

# Define the file path
data_path = "C:\\Users\\eduardo\\.xy\\startups\\INDV14.CSV"

# Read the CSV file into a DataFrame directly, specifying the delimiter
# You may need to adjust the delimiter based on your actual CSV format
df = pd.read_csv(data_path, delimiter=';', header=None)

# Extract the third column as a Series
ticks = df[2]

# Calculate the percentage change
daily_returns = ticks.pct_change(periods=1)

# Print the daily returns
print(daily_returns)

# Save the results to a new CSV file
daily_returns.to_csv('returns.csv', index=False)

endTime = datetime.now() - startTime
print(f"Processing time: {endTime}")
