
import pandas as pd
from datetime import datetime

startTime = datetime.now()

# Path to your CSV file
data_path = "C:\\Users\\eduardo\\.xy\\startups\\INDV14.CSV"

# Read the CSV file directly into a DataFrame
# Use the correct delimiter and specify the relevant columns to load
df = pd.read_csv(data_path, delimiter=';', usecols=[2], names=['Ticks'], header=None)

# Calculate the percentage change
daily_returns = df['Ticks'].pct_change()

# Save the daily returns to a new CSV file
daily_returns.to_csv('returns.csv', index=False)

# Show elapsed time
print("Time taken:", datetime.now() - startTime)
