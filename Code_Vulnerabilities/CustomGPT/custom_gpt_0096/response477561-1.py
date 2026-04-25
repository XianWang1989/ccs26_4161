
import pandas as pd
from datetime import datetime

startTime = datetime.now()

# Path to CSV file
data_path = "C:/Users/eduardo/.xy/startups/INDV14.CSV"

# Load the CSV directly into a DataFrame
# Adjust `delimiter` as needed. Here it's set to match your format.
deals = pd.read_csv(data_path, delimiter=';', header=None, usecols=[2], names=['ticks'])

# Convert the 'ticks' column to integers
deals['ticks'] = deals['ticks'].astype(int)

# Calculate the percentage change
daily_returns = deals['ticks'].pct_change()

# Save the results to a new CSV file
daily_returns.to_csv('returns.csv', index=False)

print(daily_returns)
print("Execution time:", datetime.now() - startTime)
