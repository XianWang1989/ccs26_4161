
import pandas as pd
from datetime import datetime

startTime = datetime.now()

# Path to your CSV file
data_path = "C:\\Users\\eduardo\\.xy\\startups\\INDV14.CSV"

# Read the CSV file using pandas
# Assume the delimiter is set correctly, adjust if necessary
df = pd.read_csv(data_path, delimiter=';', header=None, names=["timestamp", "tick_value", "deal"])

# Extract the third column (deals) and convert it to numeric
df['deal'] = pd.to_numeric(df['deal'], errors='coerce')

# Calculate the daily percentage change
daily_returns = df['deal'].pct_change(periods=1)

# Save results to a new CSV 
daily_returns.to_csv('returns.csv', index=False)

print(daily_returns)
print("Duration: ", datetime.now() - startTime)
