
import pandas as pd
from datetime import datetime

# Start the timer
startTime = datetime.now()

# Define the path to your CSV file
data_path = "C:\\Users\\eduardo\\.xy\\startups\\INDV14.CSV"

# Read the CSV file directly into a DataFrame
# Use ';' as the separator since your example indicates it's the delimiter
df = pd.read_csv(data_path, sep=';', header=None)  # Assuming there are no headers

# Extract the third column (index 2)
close = df[2]  # Column indexing starts from 0 in pandas

# Calculate the percentage change
daily_returns = close.pct_change(periods=1)

# Output the daily returns
print(daily_returns)

# Save daily returns to a new CSV file
daily_returns.to_csv('returns.csv', index=False, header=False)  # Save without index or header

# Stop the timer and print elapsed time
elapsed_time = datetime.now() - startTime
print(f'Time taken: {elapsed_time}')
