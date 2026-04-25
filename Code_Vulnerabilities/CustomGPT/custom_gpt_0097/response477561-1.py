
import pandas as pd
from datetime import datetime

start_time = datetime.now()

# Define the path to your CSV file
data_path = "C:\\Users\\eduardo\\.xy\\startups\\INDV14.CSV"

# Read the CSV directly into a DataFrame
# Specify the delimiter
df = pd.read_csv(data_path, delimiter=';', header=None, usecols=[2], names=['ticks'])

# Compute the percentage change
daily_returns = df['ticks'].pct_change()

# Save the results to a new CSV file
daily_returns.to_csv('returns.csv', index=False)

print(daily_returns)
print("Time taken:", datetime.now() - start_time)
