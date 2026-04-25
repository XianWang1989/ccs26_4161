
import pandas as pd
from datetime import datetime

startTime = datetime.now()

# Specify the path to your CSV file
data_path = "C:\\Users\\eduardo\\.xy\\startups\\INDV14.CSV"

# Read the CSV file into a DataFrame
df = pd.read_csv(data_path, delimiter=';', header=None)

# Extract the third column (index 2)
ticks = df[2].astype(int)

# Create a DataFrame and compute the percentage change
deals = pd.DataFrame(ticks)
daily_returns = deals.pct_change(periods=1)

# Save the daily returns to a new CSV file
daily_returns.to_csv('returns.csv', index=False)

print(daily_returns)
print("Time taken:", datetime.now() - startTime)
