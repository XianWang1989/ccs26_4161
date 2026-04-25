
import pandas as pd
from datetime import datetime

startTime = datetime.now()

# File path
data_path = r"C:\Users\eduardo\.xy\startups\INDV14.CSV"

# Read the CSV file efficiently
# Specify the correct delimiter and header
df = pd.read_csv(data_path, sep='[;]', engine='python', header=None)

# Extract the third column and convert to numeric, ignoring errors
df[2] = pd.to_numeric(df[2], errors='coerce')

# Calculate the percentage change
daily_returns = df[2].pct_change()

# Save the results to a new CSV file
daily_returns.to_csv('returns.csv', index=False)

print("Processing time:", datetime.now() - startTime)
