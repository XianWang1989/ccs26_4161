
import pandas as pd
from datetime import datetime

startTime = datetime.now()

# Define the file path to the CSV
data = "C:\\Users\\eduardo\\.xy\\startups\\INDV14.CSV"

# Load the data into a DataFrame, using the correct separator, and parse the column types
df = pd.read_csv(data, sep=';', header=None, usecols=[2], names=['ticks'], dtype={'ticks': 'int'})

# Calculate the percentage change
daily_returns = df['ticks'].pct_change()

# Print daily returns
print(daily_returns)

# Save the daily returns to a new CSV file
daily_returns.to_csv('returns.csv', index=False)

print(datetime.now() - startTime)  # Time counter
