
import pandas as pd
from datetime import datetime

startTime = datetime.now()

# Define file path
data_file = r"C:\Users\eduardo\.xy\startups\INDV14.CSV"

# Use pandas to read the CSV with proper delimiter
df = pd.read_csv(data_file, delimiter=';', header=None, names=['DateTime', 'Value', 'Tick'])

# Extract the 'Tick' column
ticks = df['Tick'].astype(int)

# Compute percentage change
daily_returns = ticks.pct_change()

# Save results to a new CSV file
daily_returns.to_csv('returns.csv', index=False, header=['Daily Returns'])

print(daily_returns)
print("Execution Time:", datetime.now() - startTime)
