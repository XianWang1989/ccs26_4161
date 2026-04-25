
import pandas as pd
from datetime import datetime

start_time = datetime.now()

# Define the path to your CSV file
data_path = "C:\\Users\\eduardo\\.xy\\startups\\INDV14.CSV"

# Read the CSV file. Specify the delimiter and select the column you need.
df = pd.read_csv(data_path, delimiter=';', usecols=[2], header=None)

# Convert the column to integers
df[0] = df[0].astype(int)

# Calculate the percentage change
daily_returns = df[0].pct_change()

# Save the daily returns to a new CSV file
daily_returns.to_csv('returns.csv', index=False, header=False)

print("Processing Time:", datetime.now() - start_time)
