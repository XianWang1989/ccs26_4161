
import pandas as pd
from datetime import datetime

startTime = datetime.now()

# Path to your CSV file
data_path = r"C:\Users\eduardo\.xy\startups\INDV14.CSV"

# Read the CSV file using pandas directly
# Specify the delimiter based on your file
df = pd.read_csv(data_path, delimiter=';', header=None)

# Extract the third column, which contains the ticks
# Assuming the ticks are in the third column (index 2)
ticks = df[2].astype(int)  # Convert to integers

# Compute percentage change
daily_returns = ticks.pct_change(periods=1)

# Save the results to a new CSV file
daily_returns.to_csv('returns.csv', index=False)

print("Time taken:", datetime.now() - startTime)
