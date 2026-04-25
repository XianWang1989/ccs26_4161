
import pandas as pd
from datetime import datetime

startTime = datetime.now()

# Define the path to your CSV file
data_path = r"C:\Users\eduardo\.xy\startups\INDV14.CSV"

# Read the CSV file using pandas
# Adjust the delimiter based on your CSV format
data = pd.read_csv(data_path, delimiter=';', header=None)

# Access the third column (index 2) directly
ticks = data[2].astype(int)  # Convert to integer

# Compute percentage change
daily_returns = ticks.pct_change(periods=1)

# Save daily returns to a new CSV file
daily_returns.to_csv('returns.csv', index=False)

print(daily_returns)
print("Time taken:", datetime.now() - startTime)
