
import pandas as pd
from datetime import datetime

start_time = datetime.now()

# Path to the CSV file
data_path = "C:\\Users\\eduardo\\.xy\\startups\\INDV14.CSV"

# Read the CSV file directly using pandas
# Specify the delimiter used in your file
# In this case, the delimiter is a combination of space and semicolon
data = pd.read_csv(data_path, sep='[ ;]', engine='python', header=None)

# Extract the third column (index 2)
close_ticks = data[2]

# Calculate the percentage change
daily_returns = close_ticks.pct_change(periods=1)

# Save the results to a new CSV file
daily_returns.to_csv('returns.csv', index=False, header=False)

# Print the time taken
print(f'Time taken: {datetime.now() - start_time}')
