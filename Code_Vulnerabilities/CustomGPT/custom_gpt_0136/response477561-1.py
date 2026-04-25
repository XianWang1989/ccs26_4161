
import pandas as pd
from datetime import datetime

# Start timer
startTime = datetime.now()

# Define the CSV file path
data_path = r"C:\Users\eduardo\.xy\startups\INDV14.CSV"

# Read the CSV file using pandas
# Use appropriate parameters for separator and header if needed
df = pd.read_csv(data_path, sep=';', header=None, usecols=[2], names=['Ticks'])

# Calculate pct_change
daily_returns = df['Ticks'].astype(float).pct_change()

# Save daily returns to a new CSV file
daily_returns.to_csv('returns.csv', index=False)

# Print the time taken
print("Processing time:", datetime.now() - startTime)
