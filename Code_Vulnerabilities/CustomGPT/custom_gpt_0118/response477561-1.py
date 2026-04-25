
import pandas as pd
from datetime import datetime

# Start timing
startTime = datetime.now()

# Define the file path
data_path = r"C:\Users\eduardo\.xy\startups\INDV14.CSV"

# Load the CSV file efficiently using pandas
# Specify the delimiter and names for the columns
df = pd.read_csv(data_path, sep=';', header=None, names=['timestamp', 'id', 'ticks'], 
                 dtype={'ticks': int}, usecols=[2])  # Only use the third column

# Calculate pct_change directly
daily_returns = df['ticks'].pct_change()

# Save the results to a new CSV file
daily_returns.to_csv('returns.csv', index=False)

# Print the time taken
print("Time taken:", datetime.now() - startTime)
