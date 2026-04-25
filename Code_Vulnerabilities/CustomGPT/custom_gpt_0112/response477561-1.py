
import pandas as pd
from datetime import datetime

startTime = datetime.now()

# File path
data_path = r"C:\Users\eduardo\.xy\startups\INDV14.CSV"

# Use pandas to read the CSV file directly
# Specify the appropriate delimiter based on your CSV format
df = pd.read_csv(data_path, delimiter=';', usecols=[2], header=None)

# Convert the column to numeric, if it's not already
df[2] = pd.to_numeric(df[2], errors='coerce')

# Calculate percentage change
daily_returns = df[2].pct_change()

# Save the results to a new CSV file
daily_returns.to_csv('returns.csv', index=False)

print("Processing time:", datetime.now() - startTime)
