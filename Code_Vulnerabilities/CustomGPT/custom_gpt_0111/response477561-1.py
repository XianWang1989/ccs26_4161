
import pandas as pd
from datetime import datetime

# Start timing
start_time = datetime.now()

# Define the path to your CSV file
data_path = "C:\\Users\\eduardo\\.xy\\startups\\INDV14.CSV"

# Read the CSV file using pandas
# Specify the delimiter as ';' to properly handle your CSV structure
# Use 'header=None' since your data does not have headers
df = pd.read_csv(data_path, delimiter=';', header=None)

# Extract the third column (index 2)
ticks = df[2]

# Convert to DataFrame and compute percentage change
deals = pd.DataFrame(ticks)
daily_returns = deals.pct_change(periods=1)

# Save the results to a new CSV file
daily_returns.to_csv('returns.csv', index=False)

# Display the time taken
print("Time taken:", datetime.now() - start_time)

# Optionally, display the daily returns
print(daily_returns)
