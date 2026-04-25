
import pandas as pd
from datetime import datetime

startTime = datetime.now()

# Define the file path
data_path = "C:\\Users\\eduardo\\.xy\\startups\\INDV14.CSV"

# Load the CSV file using pandas
df = pd.read_csv(data_path, sep=';', header=None, usecols=[2], names=['ticks'])

# Compute percentage change
daily_returns = df['ticks'].pct_change()

# Save the results to a new CSV file
daily_returns.to_csv('returns.csv', index=False)

# Print execution time
print("Execution Time:", datetime.now() - startTime)
