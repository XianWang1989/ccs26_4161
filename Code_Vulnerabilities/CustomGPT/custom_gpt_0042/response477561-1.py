
import pandas as pd
from datetime import datetime

# Start timer
startTime = datetime.now()

# Define file paths
data_path = r"C:\Users\eduardo\.xy\startups\INDV14.CSV"

# Read the CSV file directly into a DataFrame
# Specify the delimiter
df = pd.read_csv(data_path, sep=';', header=None)

# Extract the third column (index 2) and convert to numeric
df['ticks'] = pd.to_numeric(df[2], errors='coerce')

# Calculate percentage change
daily_returns = df['ticks'].pct_change()

# Save the results to a new CSV file
daily_returns.to_csv('returns.csv', index=False)

# Print out the elapsed time
print("Elapsed Time:", datetime.now() - startTime)
